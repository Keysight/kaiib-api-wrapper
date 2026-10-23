import time

import kai_inference_builder as kaiib

def create_api_client_cli(verify_ssl=True):

    import argparse
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--controller', help='The IP address or the hostname of the KAI-IB controller', required=True)
    parser.add_argument('--user', help='The username for accessing the controller, needs a password too')
    parser.add_argument('--password', help='The password for accessing the controller, needs a username too')
    args = parser.parse_args()

    """Parse the args passed to the current script and use them to create an API client; optionally disable SSL verification"""

    host = f'https://{args.controller}'

    configuration            = kaiib.Configuration(host=host,
                                                    refresh_token=None,
                                                    username=args.user,
                                                    password=args.password)
    configuration.verify_ssl = verify_ssl
    return kaiib.ApiClient(configuration)

if __name__ == "__main__":
    import urllib3; urllib3.disable_warnings()


    with create_api_client_cli(verify_ssl=True) as api_client:

        # Search for the Law Firm Legal Service default config
        api_config_instance  = kaiib.ConfigurationsApi(api_client)
        take = 1
        skip = None
        search_col = 'displayName'
        search_val = 'Law Firm Legal Service'
        filter_mode = None
        sort = None
        config = api_config_instance.get_configs(take=1,
                                                 skip=skip,
                                                 search_col=search_col,
                                                 search_val=search_val,
                                                 filter_mode=filter_mode,
                                                 sort=sort)

        if len(config.data) == 0:
            raise ValueError("Couldn't find the specified configuration.")

        api_session_instance = kaiib.SessionsApi(api_client)
        config_url = config.data[0].config_url
        sessions = [kaiib.Session(config_url=config_url)]

        # Create a session
        print("Creating empty session...")
        api_session_response = api_session_instance.create_sessions(session=sessions)
        session = api_session_response[0]
        print("Session created.\n")


        print("Adding a Sub Profile...")

        api_data_model_instance = kaiib.KAIInferenceBuilderDataModelApi(api_client)

        # adding an instance of the Contract Review sub profile to the session
        add_sub_profiles_operation = kaiib.AddSubProfilesOperation(ids=["Contract Review"])
        api_data_model_response = api_data_model_instance.start_session_config_add_sub_profiles(session.id, add_sub_profiles_operation=add_sub_profiles_operation)
        api_data_model_response.await_completion()

        print("Sub Profile added successfully.")

        print("Configuring DUT...")

        session_id = session.id
        dut_id = '1' # id of the dut, currently only one dut is supported, so the id is always 1
        dut_instance = kaiib.Dut(model = "example_model", request_url_host = "192.0.2.1", request_url_port = 8080, request_url_path = "/example_path")

        api_data_model_instance.patch_network_profile_dut(session.id, dut_id, dut=dut_instance)

        print("Configured DUT successfully.")

        print("Configuring Test Objectives...")
        # 10 Prompts per Second for 60 seconds, 5 Simulated Users

        primary_objective_instance = kaiib.PrimaryObjective(objective_value = 10, duration = 60)
        api_data_model_instance.patch_objectives_and_timeline_primary_objective(session_id, primary_objective=primary_objective_instance)

        secondary_objective_instance = kaiib.SecondaryObjective(enabled=True, objective_value=5)
        api_data_model_instance.patch_objectives_and_timeline_secondary_objective(session_id, secondary_objective=secondary_objective_instance)

        print("Configured Test Objectives successfully.")

        print("Checking available agents...")

        api_agents_instance = kaiib.AgentsApi(api_client)
        api_agents_response = api_agents_instance.get_agents()

        # pick first available agent to assign to the network
        agent_id = api_agents_response[0].id

        print("Assigning agent to the network...")

        network_id = '1' # id of the network, currently only one network is supported, so the id is always 1
        agent_instance = kaiib.AssignedAgent(agent_id = agent_id, capture_settings = kaiib.CaptureSettings(capture_enabled=True, capture_latest_packets=True, log_level=kaiib.LogLevel.INFO))
        assigned_agents = kaiib.AssignedAgents(id = '1', ids=[agent_instance])

        api_data_model_instance.patch_network_assigned_agents(session_id, network_id, assigned_agents=assigned_agents)

        print("Agent assigned to the network successfully.")

        print("Starting test ...")

        api_test_operations_instance = kaiib.TestOperationsApi(api_client)
        api_test_operation_response = api_test_operations_instance.start_test_run_start(session.id)
        api_test_operation_response.await_completion()

        print("Test started successfully.")

        session.refresh()
        while session.test.status != 'STOPPED':
            time.sleep(5)
            session.refresh()
        print("Test finished successfully.\n")

        api_reports_instance = kaiib.ReportsApi(api_client)
        result_id = session.test.test_id
        generate_pdf_report_operation = kaiib.GeneratePDFReportOperation()

        api_reports_response = api_reports_instance.start_result_generate_pdf(result_id, generate_pdf_report_operation=generate_pdf_report_operation)
        file_path = api_reports_response.await_completion()
        print(f"PDF report generated successfully. File path: {file_path}")










# kai_inference_builder.KAIInferenceBuilderDataModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_resolver_name_servers**](KAIInferenceBuilderDataModelApi.md#create_dns_resolver_name_servers) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers | 
[**create_network_ip_ranges**](KAIInferenceBuilderDataModelApi.md#create_network_ip_ranges) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges | 
[**create_network_profile_duts**](KAIInferenceBuilderDataModelApi.md#create_network_profile_duts) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts | 
[**create_network_profile_networks**](KAIInferenceBuilderDataModelApi.md#create_network_profile_networks) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks | 
[**delete_config_sub_profile**](KAIInferenceBuilderDataModelApi.md#delete_config_sub_profile) | **DELETE** /kai-ib/api/v2/sessions/{sessionId}/config/subProfiles/{subProfileId} | 
[**delete_network_ip_range**](KAIInferenceBuilderDataModelApi.md#delete_network_ip_range) | **DELETE** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges/{ipRangeId} | 
[**delete_network_profile_dut**](KAIInferenceBuilderDataModelApi.md#delete_network_profile_dut) | **DELETE** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts/{dutId} | 
[**delete_network_profile_network**](KAIInferenceBuilderDataModelApi.md#delete_network_profile_network) | **DELETE** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId} | 
[**get_assigned_agents_id_by_id**](KAIInferenceBuilderDataModelApi.md#get_assigned_agents_id_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId} | 
[**get_assigned_agents_ids**](KAIInferenceBuilderDataModelApi.md#get_assigned_agents_ids) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids | 
[**get_assigned_agents_port_by_id**](KAIInferenceBuilderDataModelApi.md#get_assigned_agents_port_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId} | 
[**get_assigned_agents_ports**](KAIInferenceBuilderDataModelApi.md#get_assigned_agents_ports) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports | 
[**get_config_network_profile**](KAIInferenceBuilderDataModelApi.md#get_config_network_profile) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile | 
[**get_config_objectives_and_timeline**](KAIInferenceBuilderDataModelApi.md#get_config_objectives_and_timeline) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline | 
[**get_config_sub_profile_by_id**](KAIInferenceBuilderDataModelApi.md#get_config_sub_profile_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/subProfiles/{subProfileId} | 
[**get_config_sub_profiles**](KAIInferenceBuilderDataModelApi.md#get_config_sub_profiles) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/subProfiles | 
[**get_dns_resolver_name_server_by_id**](KAIInferenceBuilderDataModelApi.md#get_dns_resolver_name_server_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers/{nameServerId} | 
[**get_dns_resolver_name_servers**](KAIInferenceBuilderDataModelApi.md#get_dns_resolver_name_servers) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers | 
[**get_id_capture_settings**](KAIInferenceBuilderDataModelApi.md#get_id_capture_settings) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId}/captureSettings | 
[**get_network_assigned_agents**](KAIInferenceBuilderDataModelApi.md#get_network_assigned_agents) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents | 
[**get_network_dns_resolver**](KAIInferenceBuilderDataModelApi.md#get_network_dns_resolver) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver | 
[**get_network_ip_range_by_id**](KAIInferenceBuilderDataModelApi.md#get_network_ip_range_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges/{ipRangeId} | 
[**get_network_ip_ranges**](KAIInferenceBuilderDataModelApi.md#get_network_ip_ranges) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges | 
[**get_network_profile_dut_by_id**](KAIInferenceBuilderDataModelApi.md#get_network_profile_dut_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts/{dutId} | 
[**get_network_profile_duts**](KAIInferenceBuilderDataModelApi.md#get_network_profile_duts) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts | 
[**get_network_profile_network_by_id**](KAIInferenceBuilderDataModelApi.md#get_network_profile_network_by_id) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId} | 
[**get_network_profile_networks**](KAIInferenceBuilderDataModelApi.md#get_network_profile_networks) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks | 
[**get_objectives_and_timeline_primary_objective**](KAIInferenceBuilderDataModelApi.md#get_objectives_and_timeline_primary_objective) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/primaryObjective | 
[**get_objectives_and_timeline_secondary_objective**](KAIInferenceBuilderDataModelApi.md#get_objectives_and_timeline_secondary_objective) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/secondaryObjective | 
[**get_port_capture_settings**](KAIInferenceBuilderDataModelApi.md#get_port_capture_settings) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId}/captureSettings | 
[**get_session_config**](KAIInferenceBuilderDataModelApi.md#get_session_config) | **GET** /kai-ib/api/v2/sessions/{sessionId}/config | 
[**patch_assigned_agents_id**](KAIInferenceBuilderDataModelApi.md#patch_assigned_agents_id) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId} | 
[**patch_assigned_agents_port**](KAIInferenceBuilderDataModelApi.md#patch_assigned_agents_port) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId} | 
[**patch_config_network_profile**](KAIInferenceBuilderDataModelApi.md#patch_config_network_profile) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile | 
[**patch_config_objectives_and_timeline**](KAIInferenceBuilderDataModelApi.md#patch_config_objectives_and_timeline) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline | 
[**patch_config_sub_profile**](KAIInferenceBuilderDataModelApi.md#patch_config_sub_profile) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/subProfiles/{subProfileId} | 
[**patch_dns_resolver_name_server**](KAIInferenceBuilderDataModelApi.md#patch_dns_resolver_name_server) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers/{nameServerId} | 
[**patch_id_capture_settings**](KAIInferenceBuilderDataModelApi.md#patch_id_capture_settings) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId}/captureSettings | 
[**patch_network_assigned_agents**](KAIInferenceBuilderDataModelApi.md#patch_network_assigned_agents) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents | 
[**patch_network_dns_resolver**](KAIInferenceBuilderDataModelApi.md#patch_network_dns_resolver) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver | 
[**patch_network_ip_range**](KAIInferenceBuilderDataModelApi.md#patch_network_ip_range) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges/{ipRangeId} | 
[**patch_network_profile_dut**](KAIInferenceBuilderDataModelApi.md#patch_network_profile_dut) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts/{dutId} | 
[**patch_network_profile_network**](KAIInferenceBuilderDataModelApi.md#patch_network_profile_network) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId} | 
[**patch_objectives_and_timeline_primary_objective**](KAIInferenceBuilderDataModelApi.md#patch_objectives_and_timeline_primary_objective) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/primaryObjective | 
[**patch_objectives_and_timeline_secondary_objective**](KAIInferenceBuilderDataModelApi.md#patch_objectives_and_timeline_secondary_objective) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/secondaryObjective | 
[**patch_port_capture_settings**](KAIInferenceBuilderDataModelApi.md#patch_port_capture_settings) | **PATCH** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId}/captureSettings | 
[**start_session_config_add_sub_profiles**](KAIInferenceBuilderDataModelApi.md#start_session_config_add_sub_profiles) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/operations/addSubProfiles | 
[**start_session_config_save_kai_ib_session_config**](KAIInferenceBuilderDataModelApi.md#start_session_config_save_kai_ib_session_config) | **POST** /kai-ib/api/v2/sessions/{sessionId}/config/operations/saveKaiIbSessionConfig | 
[**start_session_load_kai_ib_session_config**](KAIInferenceBuilderDataModelApi.md#start_session_load_kai_ib_session_config) | **POST** /kai-ib/api/v2/sessions/{sessionId}/operations/loadKaiIbSessionConfig | 
[**start_session_test_end**](KAIInferenceBuilderDataModelApi.md#start_session_test_end) | **POST** /kai-ib/api/v2/sessions/{sessionId}/operations/testEnd | 
[**start_session_test_init**](KAIInferenceBuilderDataModelApi.md#start_session_test_init) | **POST** /kai-ib/api/v2/sessions/{sessionId}/operations/testInit | 
[**update_assigned_agents_id**](KAIInferenceBuilderDataModelApi.md#update_assigned_agents_id) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId} | 
[**update_assigned_agents_ids**](KAIInferenceBuilderDataModelApi.md#update_assigned_agents_ids) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids | 
[**update_assigned_agents_port**](KAIInferenceBuilderDataModelApi.md#update_assigned_agents_port) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId} | 
[**update_assigned_agents_ports**](KAIInferenceBuilderDataModelApi.md#update_assigned_agents_ports) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports | 
[**update_config_network_profile**](KAIInferenceBuilderDataModelApi.md#update_config_network_profile) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile | 
[**update_config_objectives_and_timeline**](KAIInferenceBuilderDataModelApi.md#update_config_objectives_and_timeline) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline | 
[**update_config_sub_profile**](KAIInferenceBuilderDataModelApi.md#update_config_sub_profile) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/subProfiles/{subProfileId} | 
[**update_dns_resolver_name_server**](KAIInferenceBuilderDataModelApi.md#update_dns_resolver_name_server) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers/{nameServerId} | 
[**update_dns_resolver_name_servers**](KAIInferenceBuilderDataModelApi.md#update_dns_resolver_name_servers) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver/nameServers | 
[**update_id_capture_settings**](KAIInferenceBuilderDataModelApi.md#update_id_capture_settings) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ids/{idId}/captureSettings | 
[**update_network_assigned_agents**](KAIInferenceBuilderDataModelApi.md#update_network_assigned_agents) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents | 
[**update_network_dns_resolver**](KAIInferenceBuilderDataModelApi.md#update_network_dns_resolver) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/dnsResolver | 
[**update_network_ip_range**](KAIInferenceBuilderDataModelApi.md#update_network_ip_range) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges/{ipRangeId} | 
[**update_network_ip_ranges**](KAIInferenceBuilderDataModelApi.md#update_network_ip_ranges) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/ipRanges | 
[**update_network_profile_dut**](KAIInferenceBuilderDataModelApi.md#update_network_profile_dut) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/duts/{dutId} | 
[**update_network_profile_network**](KAIInferenceBuilderDataModelApi.md#update_network_profile_network) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId} | 
[**update_objectives_and_timeline_primary_objective**](KAIInferenceBuilderDataModelApi.md#update_objectives_and_timeline_primary_objective) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/primaryObjective | 
[**update_objectives_and_timeline_secondary_objective**](KAIInferenceBuilderDataModelApi.md#update_objectives_and_timeline_secondary_objective) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/objectivesAndTimeline/secondaryObjective | 
[**update_port_capture_settings**](KAIInferenceBuilderDataModelApi.md#update_port_capture_settings) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config/networkProfile/networks/{networkId}/assignedAgents/ports/{portId}/captureSettings | 
[**update_session_config**](KAIInferenceBuilderDataModelApi.md#update_session_config) | **PUT** /kai-ib/api/v2/sessions/{sessionId}/config | 


# **create_dns_resolver_name_servers**
> List[NameServer] create_dns_resolver_name_servers(session_id, network_id, name_server=name_server)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    name_server = [kai_inference_builder.NameServer()] # List[NameServer] |  (optional)

    try:
        api_response = api_instance.create_dns_resolver_name_servers(session_id, network_id, name_server=name_server)
        print("The response of KAIInferenceBuilderDataModelApi->create_dns_resolver_name_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->create_dns_resolver_name_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **name_server** | [**List[NameServer]**](NameServer.md)|  | [optional] 

### Return type

[**List[NameServer]**](NameServer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource successfully created. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_ip_ranges**
> List[IPRange] create_network_ip_ranges(session_id, network_id, ip_range=ip_range)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range = [kai_inference_builder.IPRange()] # List[IPRange] |  (optional)

    try:
        api_response = api_instance.create_network_ip_ranges(session_id, network_id, ip_range=ip_range)
        print("The response of KAIInferenceBuilderDataModelApi->create_network_ip_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->create_network_ip_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range** | [**List[IPRange]**](IPRange.md)|  | [optional] 

### Return type

[**List[IPRange]**](IPRange.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource successfully created. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_profile_duts**
> List[Dut] create_network_profile_duts(session_id, dut=dut)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dut import Dut
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    dut = [kai_inference_builder.Dut()] # List[Dut] |  (optional)

    try:
        api_response = api_instance.create_network_profile_duts(session_id, dut=dut)
        print("The response of KAIInferenceBuilderDataModelApi->create_network_profile_duts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->create_network_profile_duts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **dut** | [**List[Dut]**](Dut.md)|  | [optional] 

### Return type

[**List[Dut]**](Dut.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource successfully created. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_profile_networks**
> List[Network] create_network_profile_networks(session_id, network=network)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network import Network
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network = [kai_inference_builder.Network()] # List[Network] |  (optional)

    try:
        api_response = api_instance.create_network_profile_networks(session_id, network=network)
        print("The response of KAIInferenceBuilderDataModelApi->create_network_profile_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->create_network_profile_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network** | [**List[Network]**](Network.md)|  | [optional] 

### Return type

[**List[Network]**](Network.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource successfully created. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_sub_profile**
> delete_config_sub_profile(session_id, sub_profile_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the subprofile.

    try:
        api_instance.delete_config_sub_profile(session_id, sub_profile_id)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->delete_config_sub_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **sub_profile_id** | **str**| The ID of the subprofile. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_ip_range**
> delete_network_ip_range(session_id, network_id, ip_range_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range_id = 'ip_range_id_example' # str | The ID of the iprange.

    try:
        api_instance.delete_network_ip_range(session_id, network_id, ip_range_id)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->delete_network_ip_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range_id** | **str**| The ID of the iprange. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_profile_dut**
> delete_network_profile_dut(session_id, dut_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    dut_id = 'dut_id_example' # str | The ID of the dut.

    try:
        api_instance.delete_network_profile_dut(session_id, dut_id)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->delete_network_profile_dut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **dut_id** | **str**| The ID of the dut. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_profile_network**
> delete_network_profile_network(session_id, network_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.

    try:
        api_instance.delete_network_profile_network(session_id, network_id)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->delete_network_profile_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_agents_id_by_id**
> AssignedAgent get_assigned_agents_id_by_id(session_id, network_id, id_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agent import AssignedAgent
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.

    try:
        api_response = api_instance.get_assigned_agents_id_by_id(session_id, network_id, id_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_assigned_agents_id_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_assigned_agents_id_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 

### Return type

[**AssignedAgent**](AssignedAgent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_agents_ids**
> List[AssignedAgent] get_assigned_agents_ids(session_id, network_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agent import AssignedAgent
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_assigned_agents_ids(session_id, network_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_assigned_agents_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_assigned_agents_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[AssignedAgent]**](AssignedAgent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_agents_port_by_id**
> AssignedPort get_assigned_agents_port_by_id(session_id, network_id, port_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_port import AssignedPort
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.

    try:
        api_response = api_instance.get_assigned_agents_port_by_id(session_id, network_id, port_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_assigned_agents_port_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_assigned_agents_port_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 

### Return type

[**AssignedPort**](AssignedPort.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_agents_ports**
> List[AssignedPort] get_assigned_agents_ports(session_id, network_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_port import AssignedPort
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_assigned_agents_ports(session_id, network_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_assigned_agents_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_assigned_agents_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[AssignedPort]**](AssignedPort.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_network_profile**
> NetworkProfile get_config_network_profile(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network_profile import NetworkProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_config_network_profile(session_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_config_network_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_config_network_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**NetworkProfile**](NetworkProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_objectives_and_timeline**
> ObjectivesAndTimeline get_config_objectives_and_timeline(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.objectives_and_timeline import ObjectivesAndTimeline
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_config_objectives_and_timeline(session_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_config_objectives_and_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_config_objectives_and_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**ObjectivesAndTimeline**](ObjectivesAndTimeline.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_sub_profile_by_id**
> SubProfile get_config_sub_profile_by_id(session_id, sub_profile_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.sub_profile import SubProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the subprofile.

    try:
        api_response = api_instance.get_config_sub_profile_by_id(session_id, sub_profile_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_config_sub_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_config_sub_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **sub_profile_id** | **str**| The ID of the subprofile. | 

### Return type

[**SubProfile**](SubProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_sub_profiles**
> List[SubProfile] get_config_sub_profiles(session_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.sub_profile import SubProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_config_sub_profiles(session_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_config_sub_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_config_sub_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[SubProfile]**](SubProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_resolver_name_server_by_id**
> NameServer get_dns_resolver_name_server_by_id(session_id, network_id, name_server_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    name_server_id = 'name_server_id_example' # str | The ID of the nameserver.

    try:
        api_response = api_instance.get_dns_resolver_name_server_by_id(session_id, network_id, name_server_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_dns_resolver_name_server_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_dns_resolver_name_server_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **name_server_id** | **str**| The ID of the nameserver. | 

### Return type

[**NameServer**](NameServer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_resolver_name_servers**
> List[NameServer] get_dns_resolver_name_servers(session_id, network_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_dns_resolver_name_servers(session_id, network_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_dns_resolver_name_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_dns_resolver_name_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[NameServer]**](NameServer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_capture_settings**
> CaptureSettings get_id_capture_settings(session_id, network_id, id_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.

    try:
        api_response = api_instance.get_id_capture_settings(session_id, network_id, id_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_id_capture_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_id_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 

### Return type

[**CaptureSettings**](CaptureSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_assigned_agents**
> AssignedAgents get_network_assigned_agents(session_id, network_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agents import AssignedAgents
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.

    try:
        api_response = api_instance.get_network_assigned_agents(session_id, network_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_assigned_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_assigned_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 

### Return type

[**AssignedAgents**](AssignedAgents.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_dns_resolver**
> DNSResolver get_network_dns_resolver(session_id, network_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dns_resolver import DNSResolver
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.

    try:
        api_response = api_instance.get_network_dns_resolver(session_id, network_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_dns_resolver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_dns_resolver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 

### Return type

[**DNSResolver**](DNSResolver.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_ip_range_by_id**
> IPRange get_network_ip_range_by_id(session_id, network_id, ip_range_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range_id = 'ip_range_id_example' # str | The ID of the iprange.

    try:
        api_response = api_instance.get_network_ip_range_by_id(session_id, network_id, ip_range_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_ip_range_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_ip_range_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range_id** | **str**| The ID of the iprange. | 

### Return type

[**IPRange**](IPRange.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_ip_ranges**
> List[IPRange] get_network_ip_ranges(session_id, network_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_network_ip_ranges(session_id, network_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_ip_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_ip_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[IPRange]**](IPRange.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profile_dut_by_id**
> Dut get_network_profile_dut_by_id(session_id, dut_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dut import Dut
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    dut_id = 'dut_id_example' # str | The ID of the dut.

    try:
        api_response = api_instance.get_network_profile_dut_by_id(session_id, dut_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_profile_dut_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_profile_dut_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **dut_id** | **str**| The ID of the dut. | 

### Return type

[**Dut**](Dut.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profile_duts**
> List[Dut] get_network_profile_duts(session_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dut import Dut
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_network_profile_duts(session_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_profile_duts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_profile_duts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Dut]**](Dut.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profile_network_by_id**
> Network get_network_profile_network_by_id(session_id, network_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network import Network
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.

    try:
        api_response = api_instance.get_network_profile_network_by_id(session_id, network_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_profile_network_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_profile_network_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 

### Return type

[**Network**](Network.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | A resource with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_profile_networks**
> List[Network] get_network_profile_networks(session_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network import Network
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_network_profile_networks(session_id, take=take, skip=skip)
        print("The response of KAIInferenceBuilderDataModelApi->get_network_profile_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_network_profile_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Network]**](Network.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objectives_and_timeline_primary_objective**
> PrimaryObjective get_objectives_and_timeline_primary_objective(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.primary_objective import PrimaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_objectives_and_timeline_primary_objective(session_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_objectives_and_timeline_primary_objective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_objectives_and_timeline_primary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**PrimaryObjective**](PrimaryObjective.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objectives_and_timeline_secondary_objective**
> SecondaryObjective get_objectives_and_timeline_secondary_objective(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.secondary_objective import SecondaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_objectives_and_timeline_secondary_objective(session_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_objectives_and_timeline_secondary_objective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_objectives_and_timeline_secondary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**SecondaryObjective**](SecondaryObjective.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_capture_settings**
> CaptureSettings get_port_capture_settings(session_id, network_id, port_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.

    try:
        api_response = api_instance.get_port_capture_settings(session_id, network_id, port_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_port_capture_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_port_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 

### Return type

[**CaptureSettings**](CaptureSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_config**
> KAIIBConfig get_session_config(session_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.kaiib_config import KAIIBConfig
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.get_session_config(session_id)
        print("The response of KAIInferenceBuilderDataModelApi->get_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->get_session_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

### Return type

[**KAIIBConfig**](KAIIBConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_assigned_agents_id**
> patch_assigned_agents_id(session_id, network_id, id_id, assigned_agent=assigned_agent)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agent import AssignedAgent
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.
    assigned_agent = kai_inference_builder.AssignedAgent() # AssignedAgent |  (optional)

    try:
        api_instance.patch_assigned_agents_id(session_id, network_id, id_id, assigned_agent=assigned_agent)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_assigned_agents_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 
 **assigned_agent** | [**AssignedAgent**](AssignedAgent.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_assigned_agents_port**
> patch_assigned_agents_port(session_id, network_id, port_id, assigned_port=assigned_port)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_port import AssignedPort
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.
    assigned_port = kai_inference_builder.AssignedPort() # AssignedPort |  (optional)

    try:
        api_instance.patch_assigned_agents_port(session_id, network_id, port_id, assigned_port=assigned_port)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_assigned_agents_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 
 **assigned_port** | [**AssignedPort**](AssignedPort.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_network_profile**
> patch_config_network_profile(session_id, network_profile=network_profile)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network_profile import NetworkProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_profile = kai_inference_builder.NetworkProfile() # NetworkProfile |  (optional)

    try:
        api_instance.patch_config_network_profile(session_id, network_profile=network_profile)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_config_network_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_profile** | [**NetworkProfile**](NetworkProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_objectives_and_timeline**
> patch_config_objectives_and_timeline(session_id, objectives_and_timeline=objectives_and_timeline)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.objectives_and_timeline import ObjectivesAndTimeline
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    objectives_and_timeline = kai_inference_builder.ObjectivesAndTimeline() # ObjectivesAndTimeline |  (optional)

    try:
        api_instance.patch_config_objectives_and_timeline(session_id, objectives_and_timeline=objectives_and_timeline)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_config_objectives_and_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **objectives_and_timeline** | [**ObjectivesAndTimeline**](ObjectivesAndTimeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_sub_profile**
> patch_config_sub_profile(session_id, sub_profile_id, sub_profile=sub_profile)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.sub_profile import SubProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the subprofile.
    sub_profile = kai_inference_builder.SubProfile() # SubProfile |  (optional)

    try:
        api_instance.patch_config_sub_profile(session_id, sub_profile_id, sub_profile=sub_profile)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_config_sub_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **sub_profile_id** | **str**| The ID of the subprofile. | 
 **sub_profile** | [**SubProfile**](SubProfile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dns_resolver_name_server**
> patch_dns_resolver_name_server(session_id, network_id, name_server_id, name_server=name_server)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    name_server_id = 'name_server_id_example' # str | The ID of the nameserver.
    name_server = kai_inference_builder.NameServer() # NameServer |  (optional)

    try:
        api_instance.patch_dns_resolver_name_server(session_id, network_id, name_server_id, name_server=name_server)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_dns_resolver_name_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **name_server_id** | **str**| The ID of the nameserver. | 
 **name_server** | [**NameServer**](NameServer.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_id_capture_settings**
> patch_id_capture_settings(session_id, network_id, id_id, capture_settings=capture_settings)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.
    capture_settings = kai_inference_builder.CaptureSettings() # CaptureSettings |  (optional)

    try:
        api_instance.patch_id_capture_settings(session_id, network_id, id_id, capture_settings=capture_settings)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_id_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 
 **capture_settings** | [**CaptureSettings**](CaptureSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_assigned_agents**
> patch_network_assigned_agents(session_id, network_id, assigned_agents=assigned_agents)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agents import AssignedAgents
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    assigned_agents = kai_inference_builder.AssignedAgents() # AssignedAgents |  (optional)

    try:
        api_instance.patch_network_assigned_agents(session_id, network_id, assigned_agents=assigned_agents)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_network_assigned_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **assigned_agents** | [**AssignedAgents**](AssignedAgents.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_dns_resolver**
> patch_network_dns_resolver(session_id, network_id, dns_resolver=dns_resolver)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dns_resolver import DNSResolver
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    dns_resolver = kai_inference_builder.DNSResolver() # DNSResolver |  (optional)

    try:
        api_instance.patch_network_dns_resolver(session_id, network_id, dns_resolver=dns_resolver)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_network_dns_resolver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **dns_resolver** | [**DNSResolver**](DNSResolver.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_ip_range**
> patch_network_ip_range(session_id, network_id, ip_range_id, ip_range=ip_range)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range_id = 'ip_range_id_example' # str | The ID of the iprange.
    ip_range = kai_inference_builder.IPRange() # IPRange |  (optional)

    try:
        api_instance.patch_network_ip_range(session_id, network_id, ip_range_id, ip_range=ip_range)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_network_ip_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range_id** | **str**| The ID of the iprange. | 
 **ip_range** | [**IPRange**](IPRange.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_profile_dut**
> patch_network_profile_dut(session_id, dut_id, dut=dut)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dut import Dut
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    dut_id = 'dut_id_example' # str | The ID of the dut.
    dut = kai_inference_builder.Dut() # Dut |  (optional)

    try:
        api_instance.patch_network_profile_dut(session_id, dut_id, dut=dut)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_network_profile_dut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **dut_id** | **str**| The ID of the dut. | 
 **dut** | [**Dut**](Dut.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_profile_network**
> patch_network_profile_network(session_id, network_id, network=network)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network import Network
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    network = kai_inference_builder.Network() # Network |  (optional)

    try:
        api_instance.patch_network_profile_network(session_id, network_id, network=network)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_network_profile_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **network** | [**Network**](Network.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_objectives_and_timeline_primary_objective**
> patch_objectives_and_timeline_primary_objective(session_id, primary_objective=primary_objective)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.primary_objective import PrimaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    primary_objective = kai_inference_builder.PrimaryObjective() # PrimaryObjective |  (optional)

    try:
        api_instance.patch_objectives_and_timeline_primary_objective(session_id, primary_objective=primary_objective)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_objectives_and_timeline_primary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **primary_objective** | [**PrimaryObjective**](PrimaryObjective.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_objectives_and_timeline_secondary_objective**
> patch_objectives_and_timeline_secondary_objective(session_id, secondary_objective=secondary_objective)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.secondary_objective import SecondaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    secondary_objective = kai_inference_builder.SecondaryObjective() # SecondaryObjective |  (optional)

    try:
        api_instance.patch_objectives_and_timeline_secondary_objective(session_id, secondary_objective=secondary_objective)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_objectives_and_timeline_secondary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **secondary_objective** | [**SecondaryObjective**](SecondaryObjective.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_port_capture_settings**
> patch_port_capture_settings(session_id, network_id, port_id, capture_settings=capture_settings)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.
    capture_settings = kai_inference_builder.CaptureSettings() # CaptureSettings |  (optional)

    try:
        api_instance.patch_port_capture_settings(session_id, network_id, port_id, capture_settings=capture_settings)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->patch_port_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 
 **capture_settings** | [**CaptureSettings**](CaptureSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was completed successfully. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_config_add_sub_profiles**
> AsyncContext start_session_config_add_sub_profiles(session_id, add_sub_profiles_operation=add_sub_profiles_operation)



This operation adds sub profiles to the current session configuration.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.add_sub_profiles_operation import AddSubProfilesOperation
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    add_sub_profiles_operation = kai_inference_builder.AddSubProfilesOperation() # AddSubProfilesOperation |  (optional)

    try:
        api_response = api_instance.start_session_config_add_sub_profiles(session_id, add_sub_profiles_operation=add_sub_profiles_operation)
        print("The response of KAIInferenceBuilderDataModelApi->start_session_config_add_sub_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->start_session_config_add_sub_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **add_sub_profiles_operation** | [**AddSubProfilesOperation**](AddSubProfilesOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_config_save_kai_ib_session_config**
> AsyncContext start_session_config_save_kai_ib_session_config(session_id, config_id, save_config_operation=save_config_operation)



This operation saves the configuration of the current session using the specified name.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.save_config_operation import SaveConfigOperation
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    config_id = 'config_id_example' # str | The ID of the config.
    save_config_operation = kai_inference_builder.SaveConfigOperation() # SaveConfigOperation |  (optional)

    try:
        api_response = api_instance.start_session_config_save_kai_ib_session_config(session_id, config_id, save_config_operation=save_config_operation)
        print("The response of KAIInferenceBuilderDataModelApi->start_session_config_save_kai_ib_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->start_session_config_save_kai_ib_session_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **config_id** | **str**| The ID of the config. | 
 **save_config_operation** | [**SaveConfigOperation**](SaveConfigOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_load_kai_ib_session_config**
> AsyncContext start_session_load_kai_ib_session_config(session_id, load_config_operation=load_config_operation)



This operation loads the specified config into the current session

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.load_config_operation import LoadConfigOperation
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    load_config_operation = [kai_inference_builder.LoadConfigOperation()] # List[LoadConfigOperation] |  (optional)

    try:
        api_response = api_instance.start_session_load_kai_ib_session_config(session_id, load_config_operation=load_config_operation)
        print("The response of KAIInferenceBuilderDataModelApi->start_session_load_kai_ib_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->start_session_load_kai_ib_session_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **load_config_operation** | [**List[LoadConfigOperation]**](LoadConfigOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_test_end**
> AsyncContext start_session_test_end(session_id, test_state_changed_operation=test_state_changed_operation)



This is called from traffic controller to notify that a test has ended. It should return any information needed by the traffic controller to completely clean up the test.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.test_state_changed_operation import TestStateChangedOperation
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_state_changed_operation = [kai_inference_builder.TestStateChangedOperation()] # List[TestStateChangedOperation] |  (optional)

    try:
        api_response = api_instance.start_session_test_end(session_id, test_state_changed_operation=test_state_changed_operation)
        print("The response of KAIInferenceBuilderDataModelApi->start_session_test_end:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->start_session_test_end: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_state_changed_operation** | [**List[TestStateChangedOperation]**](TestStateChangedOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session_test_init**
> AsyncContext start_session_test_init(session_id, test_state_changed_operation=test_state_changed_operation)



This is called from traffic controller to notify that a new test is starting. It should return all the information needed by the traffic controller to start the test.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.test_state_changed_operation import TestStateChangedOperation
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    test_state_changed_operation = [kai_inference_builder.TestStateChangedOperation()] # List[TestStateChangedOperation] |  (optional)

    try:
        api_response = api_instance.start_session_test_init(session_id, test_state_changed_operation=test_state_changed_operation)
        print("The response of KAIInferenceBuilderDataModelApi->start_session_test_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->start_session_test_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **test_state_changed_operation** | [**List[TestStateChangedOperation]**](TestStateChangedOperation.md)|  | [optional] 

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assigned_agents_id**
> AssignedAgent update_assigned_agents_id(session_id, network_id, id_id, assigned_agent=assigned_agent)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agent import AssignedAgent
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.
    assigned_agent = kai_inference_builder.AssignedAgent() # AssignedAgent |  (optional)

    try:
        api_response = api_instance.update_assigned_agents_id(session_id, network_id, id_id, assigned_agent=assigned_agent)
        print("The response of KAIInferenceBuilderDataModelApi->update_assigned_agents_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_assigned_agents_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 
 **assigned_agent** | [**AssignedAgent**](AssignedAgent.md)|  | [optional] 

### Return type

[**AssignedAgent**](AssignedAgent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assigned_agents_ids**
> List[AssignedAgent] update_assigned_agents_ids(session_id, network_id, assigned_agent=assigned_agent)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agent import AssignedAgent
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    assigned_agent = [kai_inference_builder.AssignedAgent()] # List[AssignedAgent] |  (optional)

    try:
        api_response = api_instance.update_assigned_agents_ids(session_id, network_id, assigned_agent=assigned_agent)
        print("The response of KAIInferenceBuilderDataModelApi->update_assigned_agents_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_assigned_agents_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **assigned_agent** | [**List[AssignedAgent]**](AssignedAgent.md)|  | [optional] 

### Return type

[**List[AssignedAgent]**](AssignedAgent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assigned_agents_port**
> AssignedPort update_assigned_agents_port(session_id, network_id, port_id, assigned_port=assigned_port)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_port import AssignedPort
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.
    assigned_port = kai_inference_builder.AssignedPort() # AssignedPort |  (optional)

    try:
        api_response = api_instance.update_assigned_agents_port(session_id, network_id, port_id, assigned_port=assigned_port)
        print("The response of KAIInferenceBuilderDataModelApi->update_assigned_agents_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_assigned_agents_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 
 **assigned_port** | [**AssignedPort**](AssignedPort.md)|  | [optional] 

### Return type

[**AssignedPort**](AssignedPort.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assigned_agents_ports**
> List[AssignedPort] update_assigned_agents_ports(session_id, network_id, assigned_port=assigned_port)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_port import AssignedPort
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    assigned_port = [kai_inference_builder.AssignedPort()] # List[AssignedPort] |  (optional)

    try:
        api_response = api_instance.update_assigned_agents_ports(session_id, network_id, assigned_port=assigned_port)
        print("The response of KAIInferenceBuilderDataModelApi->update_assigned_agents_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_assigned_agents_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **assigned_port** | [**List[AssignedPort]**](AssignedPort.md)|  | [optional] 

### Return type

[**List[AssignedPort]**](AssignedPort.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_network_profile**
> NetworkProfile update_config_network_profile(session_id, network_profile=network_profile)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network_profile import NetworkProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_profile = kai_inference_builder.NetworkProfile() # NetworkProfile |  (optional)

    try:
        api_response = api_instance.update_config_network_profile(session_id, network_profile=network_profile)
        print("The response of KAIInferenceBuilderDataModelApi->update_config_network_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_config_network_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_profile** | [**NetworkProfile**](NetworkProfile.md)|  | [optional] 

### Return type

[**NetworkProfile**](NetworkProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_objectives_and_timeline**
> ObjectivesAndTimeline update_config_objectives_and_timeline(session_id, objectives_and_timeline=objectives_and_timeline)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.objectives_and_timeline import ObjectivesAndTimeline
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    objectives_and_timeline = kai_inference_builder.ObjectivesAndTimeline() # ObjectivesAndTimeline |  (optional)

    try:
        api_response = api_instance.update_config_objectives_and_timeline(session_id, objectives_and_timeline=objectives_and_timeline)
        print("The response of KAIInferenceBuilderDataModelApi->update_config_objectives_and_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_config_objectives_and_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **objectives_and_timeline** | [**ObjectivesAndTimeline**](ObjectivesAndTimeline.md)|  | [optional] 

### Return type

[**ObjectivesAndTimeline**](ObjectivesAndTimeline.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_sub_profile**
> SubProfile update_config_sub_profile(session_id, sub_profile_id, sub_profile=sub_profile)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.sub_profile import SubProfile
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the subprofile.
    sub_profile = kai_inference_builder.SubProfile() # SubProfile |  (optional)

    try:
        api_response = api_instance.update_config_sub_profile(session_id, sub_profile_id, sub_profile=sub_profile)
        print("The response of KAIInferenceBuilderDataModelApi->update_config_sub_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_config_sub_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **sub_profile_id** | **str**| The ID of the subprofile. | 
 **sub_profile** | [**SubProfile**](SubProfile.md)|  | [optional] 

### Return type

[**SubProfile**](SubProfile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_resolver_name_server**
> NameServer update_dns_resolver_name_server(session_id, network_id, name_server_id, name_server=name_server)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    name_server_id = 'name_server_id_example' # str | The ID of the nameserver.
    name_server = kai_inference_builder.NameServer() # NameServer |  (optional)

    try:
        api_response = api_instance.update_dns_resolver_name_server(session_id, network_id, name_server_id, name_server=name_server)
        print("The response of KAIInferenceBuilderDataModelApi->update_dns_resolver_name_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_dns_resolver_name_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **name_server_id** | **str**| The ID of the nameserver. | 
 **name_server** | [**NameServer**](NameServer.md)|  | [optional] 

### Return type

[**NameServer**](NameServer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_resolver_name_servers**
> List[NameServer] update_dns_resolver_name_servers(session_id, network_id, name_server=name_server)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.name_server import NameServer
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    name_server = [kai_inference_builder.NameServer()] # List[NameServer] |  (optional)

    try:
        api_response = api_instance.update_dns_resolver_name_servers(session_id, network_id, name_server=name_server)
        print("The response of KAIInferenceBuilderDataModelApi->update_dns_resolver_name_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_dns_resolver_name_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **name_server** | [**List[NameServer]**](NameServer.md)|  | [optional] 

### Return type

[**List[NameServer]**](NameServer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_id_capture_settings**
> CaptureSettings update_id_capture_settings(session_id, network_id, id_id, capture_settings=capture_settings)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    id_id = 'id_id_example' # str | The ID of the id.
    capture_settings = kai_inference_builder.CaptureSettings() # CaptureSettings |  (optional)

    try:
        api_response = api_instance.update_id_capture_settings(session_id, network_id, id_id, capture_settings=capture_settings)
        print("The response of KAIInferenceBuilderDataModelApi->update_id_capture_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_id_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **id_id** | **str**| The ID of the id. | 
 **capture_settings** | [**CaptureSettings**](CaptureSettings.md)|  | [optional] 

### Return type

[**CaptureSettings**](CaptureSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_assigned_agents**
> AssignedAgents update_network_assigned_agents(session_id, network_id, assigned_agents=assigned_agents)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.assigned_agents import AssignedAgents
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    assigned_agents = kai_inference_builder.AssignedAgents() # AssignedAgents |  (optional)

    try:
        api_response = api_instance.update_network_assigned_agents(session_id, network_id, assigned_agents=assigned_agents)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_assigned_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_assigned_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **assigned_agents** | [**AssignedAgents**](AssignedAgents.md)|  | [optional] 

### Return type

[**AssignedAgents**](AssignedAgents.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_dns_resolver**
> DNSResolver update_network_dns_resolver(session_id, network_id, dns_resolver=dns_resolver)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dns_resolver import DNSResolver
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    dns_resolver = kai_inference_builder.DNSResolver() # DNSResolver |  (optional)

    try:
        api_response = api_instance.update_network_dns_resolver(session_id, network_id, dns_resolver=dns_resolver)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_dns_resolver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_dns_resolver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **dns_resolver** | [**DNSResolver**](DNSResolver.md)|  | [optional] 

### Return type

[**DNSResolver**](DNSResolver.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_ip_range**
> IPRange update_network_ip_range(session_id, network_id, ip_range_id, ip_range=ip_range)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range_id = 'ip_range_id_example' # str | The ID of the iprange.
    ip_range = kai_inference_builder.IPRange() # IPRange |  (optional)

    try:
        api_response = api_instance.update_network_ip_range(session_id, network_id, ip_range_id, ip_range=ip_range)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_ip_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_ip_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range_id** | **str**| The ID of the iprange. | 
 **ip_range** | [**IPRange**](IPRange.md)|  | [optional] 

### Return type

[**IPRange**](IPRange.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_ip_ranges**
> List[IPRange] update_network_ip_ranges(session_id, network_id, ip_range=ip_range)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.ip_range import IPRange
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    ip_range = [kai_inference_builder.IPRange()] # List[IPRange] |  (optional)

    try:
        api_response = api_instance.update_network_ip_ranges(session_id, network_id, ip_range=ip_range)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_ip_ranges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_ip_ranges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **ip_range** | [**List[IPRange]**](IPRange.md)|  | [optional] 

### Return type

[**List[IPRange]**](IPRange.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_profile_dut**
> Dut update_network_profile_dut(session_id, dut_id, dut=dut)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.dut import Dut
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    dut_id = 'dut_id_example' # str | The ID of the dut.
    dut = kai_inference_builder.Dut() # Dut |  (optional)

    try:
        api_response = api_instance.update_network_profile_dut(session_id, dut_id, dut=dut)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_profile_dut:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_profile_dut: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **dut_id** | **str**| The ID of the dut. | 
 **dut** | [**Dut**](Dut.md)|  | [optional] 

### Return type

[**Dut**](Dut.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_profile_network**
> Network update_network_profile_network(session_id, network_id, network=network)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.network import Network
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    network = kai_inference_builder.Network() # Network |  (optional)

    try:
        api_response = api_instance.update_network_profile_network(session_id, network_id, network=network)
        print("The response of KAIInferenceBuilderDataModelApi->update_network_profile_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_network_profile_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **network** | [**Network**](Network.md)|  | [optional] 

### Return type

[**Network**](Network.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_objectives_and_timeline_primary_objective**
> PrimaryObjective update_objectives_and_timeline_primary_objective(session_id, primary_objective=primary_objective)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.primary_objective import PrimaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    primary_objective = kai_inference_builder.PrimaryObjective() # PrimaryObjective |  (optional)

    try:
        api_response = api_instance.update_objectives_and_timeline_primary_objective(session_id, primary_objective=primary_objective)
        print("The response of KAIInferenceBuilderDataModelApi->update_objectives_and_timeline_primary_objective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_objectives_and_timeline_primary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **primary_objective** | [**PrimaryObjective**](PrimaryObjective.md)|  | [optional] 

### Return type

[**PrimaryObjective**](PrimaryObjective.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_objectives_and_timeline_secondary_objective**
> SecondaryObjective update_objectives_and_timeline_secondary_objective(session_id, secondary_objective=secondary_objective)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.secondary_objective import SecondaryObjective
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    secondary_objective = kai_inference_builder.SecondaryObjective() # SecondaryObjective |  (optional)

    try:
        api_response = api_instance.update_objectives_and_timeline_secondary_objective(session_id, secondary_objective=secondary_objective)
        print("The response of KAIInferenceBuilderDataModelApi->update_objectives_and_timeline_secondary_objective:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_objectives_and_timeline_secondary_objective: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **secondary_objective** | [**SecondaryObjective**](SecondaryObjective.md)|  | [optional] 

### Return type

[**SecondaryObjective**](SecondaryObjective.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_port_capture_settings**
> CaptureSettings update_port_capture_settings(session_id, network_id, port_id, capture_settings=capture_settings)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.capture_settings import CaptureSettings
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    network_id = 'network_id_example' # str | The ID of the network.
    port_id = 'port_id_example' # str | The ID of the port.
    capture_settings = kai_inference_builder.CaptureSettings() # CaptureSettings |  (optional)

    try:
        api_response = api_instance.update_port_capture_settings(session_id, network_id, port_id, capture_settings=capture_settings)
        print("The response of KAIInferenceBuilderDataModelApi->update_port_capture_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_port_capture_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **network_id** | **str**| The ID of the network. | 
 **port_id** | **str**| The ID of the port. | 
 **capture_settings** | [**CaptureSettings**](CaptureSettings.md)|  | [optional] 

### Return type

[**CaptureSettings**](CaptureSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_session_config**
> KAIIBConfig update_session_config(session_id, kaiib_config=kaiib_config)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.kaiib_config import KAIIBConfig
from kai_inference_builder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kai_inference_builder.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

configuration.refresh_token = os.environ["OFFLINE_TOKEN_FROM_KAI_IB_UI"]

# Enter a context with an instance of the API client
with kai_inference_builder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kai_inference_builder.KAIInferenceBuilderDataModelApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.
    kaiib_config = kai_inference_builder.KAIIBConfig() # KAIIBConfig |  (optional)

    try:
        api_response = api_instance.update_session_config(session_id, kaiib_config=kaiib_config)
        print("The response of KAIInferenceBuilderDataModelApi->update_session_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KAIInferenceBuilderDataModelApi->update_session_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 
 **kaiib_config** | [**KAIIBConfig**](KAIIBConfig.md)|  | [optional] 

### Return type

[**KAIIBConfig**](KAIIBConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


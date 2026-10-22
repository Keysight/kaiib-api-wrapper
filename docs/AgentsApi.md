# kai_inference_builder.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent**](AgentsApi.md#delete_agent) | **DELETE** /kai-ib/api/v2/agents/{agentId} | 
[**get_agent_by_id**](AgentsApi.md#get_agent_by_id) | **GET** /kai-ib/api/v2/agents/{agentId} | 
[**get_agents**](AgentsApi.md#get_agents) | **GET** /kai-ib/api/v2/agents | 
[**get_compute_node_port_by_id**](AgentsApi.md#get_compute_node_port_by_id) | **GET** /kai-ib/api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId}/ports/{portId} | 
[**get_compute_node_ports**](AgentsApi.md#get_compute_node_ports) | **GET** /kai-ib/api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId}/ports | 
[**get_controller_by_id**](AgentsApi.md#get_controller_by_id) | **GET** /kai-ib/api/v2/controllers/{controllerId} | 
[**get_controller_compute_node_by_id**](AgentsApi.md#get_controller_compute_node_by_id) | **GET** /kai-ib/api/v2/controllers/{controllerId}/compute-nodes/{computeNodeId} | 
[**get_controller_compute_nodes**](AgentsApi.md#get_controller_compute_nodes) | **GET** /kai-ib/api/v2/controllers/{controllerId}/compute-nodes | 
[**get_controllers**](AgentsApi.md#get_controllers) | **GET** /kai-ib/api/v2/controllers | 
[**get_tags**](AgentsApi.md#get_tags) | **GET** /kai-ib/api/v2/tags | 
[**patch_agent**](AgentsApi.md#patch_agent) | **PATCH** /kai-ib/api/v2/agents/{agentId} | 
[**start_agents_batch_delete**](AgentsApi.md#start_agents_batch_delete) | **POST** /kai-ib/api/v2/agents/operations/batch-delete | 
[**start_agents_export_files**](AgentsApi.md#start_agents_export_files) | **POST** /kai-ib/api/v2/agents/operations/exportFiles | 
[**start_agents_reboot**](AgentsApi.md#start_agents_reboot) | **POST** /kai-ib/api/v2/agents/operations/reboot | 
[**start_agents_release**](AgentsApi.md#start_agents_release) | **POST** /kai-ib/api/v2/agents/operations/release | 
[**start_agents_reserve**](AgentsApi.md#start_agents_reserve) | **POST** /kai-ib/api/v2/agents/operations/reserve | 
[**start_agents_set_dpdk_mode**](AgentsApi.md#start_agents_set_dpdk_mode) | **POST** /kai-ib/api/v2/agents/operations/set-dpdk-mode | 
[**start_agents_set_ntp**](AgentsApi.md#start_agents_set_ntp) | **POST** /kai-ib/api/v2/agents/operations/set-ntp | 
[**start_agents_update**](AgentsApi.md#start_agents_update) | **POST** /kai-ib/api/v2/agents/operations/update | 
[**start_controllers_clear_port_ownership**](AgentsApi.md#start_controllers_clear_port_ownership) | **POST** /kai-ib/api/v2/controllers/operations/clear-port-ownership | 
[**start_controllers_power_cycle_nodes**](AgentsApi.md#start_controllers_power_cycle_nodes) | **POST** /kai-ib/api/v2/controllers/operations/power-cycle-nodes | 
[**start_controllers_reboot_port**](AgentsApi.md#start_controllers_reboot_port) | **POST** /kai-ib/api/v2/controllers/operations/reboot-port | 
[**start_controllers_set_app**](AgentsApi.md#start_controllers_set_app) | **POST** /kai-ib/api/v2/controllers/operations/set-app | 
[**start_controllers_set_node_aggregation**](AgentsApi.md#start_controllers_set_node_aggregation) | **POST** /kai-ib/api/v2/controllers/operations/set-node-aggregation | 
[**start_controllers_set_node_app**](AgentsApi.md#start_controllers_set_node_app) | **POST** /kai-ib/api/v2/controllers/operations/set-node-app | 
[**start_controllers_set_port_link_state**](AgentsApi.md#start_controllers_set_port_link_state) | **POST** /kai-ib/api/v2/controllers/operations/set-port-link-state | 
[**start_controllers_update_port_tags**](AgentsApi.md#start_controllers_update_port_tags) | **POST** /kai-ib/api/v2/controllers/operations/update-port-tags | 


# **delete_agent**
> delete_agent(agent_id)



Remove a particular agent.

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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_instance.delete_agent(agent_id)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

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
**204** | The agent was successfully removed. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_by_id**
> Agent get_agent_by_id(agent_id)



Get a particular agent.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.agent import Agent
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.

    try:
        api_response = api_instance.get_agent_by_id(agent_id)
        print("The response of AgentsApi->get_agent_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 

### Return type

[**Agent**](Agent.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested agent |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> List[Agent] get_agents(take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.agent import Agent
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_agents(take=take, skip=skip)
        print("The response of AgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Agent]**](Agent.md)

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

# **get_compute_node_port_by_id**
> Port get_compute_node_port_by_id(controller_id, compute_node_id, port_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.port import Port
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.
    port_id = 'port_id_example' # str | The ID of the port.

    try:
        api_response = api_instance.get_compute_node_port_by_id(controller_id, compute_node_id, port_id)
        print("The response of AgentsApi->get_compute_node_port_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_compute_node_port_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 
 **port_id** | **str**| The ID of the port. | 

### Return type

[**Port**](Port.md)

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

# **get_compute_node_ports**
> List[Port] get_compute_node_ports(controller_id, compute_node_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.port import Port
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_compute_node_ports(controller_id, compute_node_id, take=take, skip=skip)
        print("The response of AgentsApi->get_compute_node_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_compute_node_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Port]**](Port.md)

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

# **get_controller_by_id**
> Controller get_controller_by_id(controller_id)



Get the controller chain.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.controller import Controller
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.

    try:
        api_response = api_instance.get_controller_by_id(controller_id)
        print("The response of AgentsApi->get_controller_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controller_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 

### Return type

[**Controller**](Controller.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The controller chain. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_controller_compute_node_by_id**
> ComputeNode get_controller_compute_node_by_id(controller_id, compute_node_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.compute_node import ComputeNode
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    compute_node_id = 'compute_node_id_example' # str | The ID of the compute node.

    try:
        api_response = api_instance.get_controller_compute_node_by_id(controller_id, compute_node_id)
        print("The response of AgentsApi->get_controller_compute_node_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controller_compute_node_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **compute_node_id** | **str**| The ID of the compute node. | 

### Return type

[**ComputeNode**](ComputeNode.md)

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

# **get_controller_compute_nodes**
> List[ComputeNode] get_controller_compute_nodes(controller_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.compute_node import ComputeNode
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    controller_id = 'controller_id_example' # str | The ID of the controller.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_controller_compute_nodes(controller_id, take=take, skip=skip)
        print("The response of AgentsApi->get_controller_compute_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controller_compute_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | **str**| The ID of the controller. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[ComputeNode]**](ComputeNode.md)

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

# **get_controllers**
> GetControllers200Response get_controllers(take=take, skip=skip, include=include)



Get the controllers chain.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_controllers200_response import GetControllers200Response
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)
    include = 'include_example' # str | Specifies if the sub-fields that are objects should be included. (optional)

    try:
        api_response = api_instance.get_controllers(take=take, skip=skip, include=include)
        print("The response of AgentsApi->get_controllers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_controllers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 
 **include** | **str**| Specifies if the sub-fields that are objects should be included. | [optional] 

### Return type

[**GetControllers200Response**](GetControllers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of controllers. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> GetTags200Response get_tags(take=take, skip=skip)



Get all the currently available agent groups.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_tags200_response import GetTags200Response
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_tags(take=take, skip=skip)
        print("The response of AgentsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetTags200Response**](GetTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of agent groups |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent**
> patch_agent(agent_id, agent=agent)



Update a particular agent. Only non-null fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.agent import Agent
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | The ID of the agent.
    agent = kai_inference_builder.Agent() # Agent |  (optional)

    try:
        api_instance.patch_agent(agent_id, agent=agent)
    except Exception as e:
        print("Exception when calling AgentsApi->patch_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| The ID of the agent. | 
 **agent** | [**Agent**](Agent.md)|  | [optional] 

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
**204** | The agent was successfully updated. |  -  |
**404** | An agent with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_agents_batch_delete**
> AsyncContext start_agents_batch_delete(start_agents_batch_delete_request_inner=start_agents_batch_delete_request_inner)



Remove multiple agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.start_agents_batch_delete_request_inner import StartAgentsBatchDeleteRequestInner
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    start_agents_batch_delete_request_inner = [kai_inference_builder.StartAgentsBatchDeleteRequestInner()] # List[StartAgentsBatchDeleteRequestInner] |  (optional)

    try:
        api_response = api_instance.start_agents_batch_delete(start_agents_batch_delete_request_inner=start_agents_batch_delete_request_inner)
        print("The response of AgentsApi->start_agents_batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_agents_batch_delete_request_inner** | [**List[StartAgentsBatchDeleteRequestInner]**](StartAgentsBatchDeleteRequestInner.md)|  | [optional] 

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

# **start_agents_export_files**
> AsyncContext start_agents_export_files(export_files_operation_input=export_files_operation_input)



Sends export files requests to a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.export_files_operation_input import ExportFilesOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    export_files_operation_input = kai_inference_builder.ExportFilesOperationInput() # ExportFilesOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_export_files(export_files_operation_input=export_files_operation_input)
        print("The response of AgentsApi->start_agents_export_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_export_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_files_operation_input** | [**ExportFilesOperationInput**](ExportFilesOperationInput.md)|  | [optional] 

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

# **start_agents_reboot**
> AsyncContext start_agents_reboot(reboot_operation_input=reboot_operation_input)



Reboot the agents specified in the request.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.reboot_operation_input import RebootOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    reboot_operation_input = kai_inference_builder.RebootOperationInput() # RebootOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_reboot(reboot_operation_input=reboot_operation_input)
        print("The response of AgentsApi->start_agents_reboot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_reboot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_operation_input** | [**RebootOperationInput**](RebootOperationInput.md)|  | [optional] 

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

# **start_agents_release**
> AsyncContext start_agents_release(release_operation_input=release_operation_input)



Releases all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.release_operation_input import ReleaseOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    release_operation_input = kai_inference_builder.ReleaseOperationInput() # ReleaseOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_release(release_operation_input=release_operation_input)
        print("The response of AgentsApi->start_agents_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_operation_input** | [**ReleaseOperationInput**](ReleaseOperationInput.md)|  | [optional] 

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

# **start_agents_reserve**
> AsyncContext start_agents_reserve(reserve_operation_input=reserve_operation_input)



Reserves all the agents from the given session.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.reserve_operation_input import ReserveOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    reserve_operation_input = kai_inference_builder.ReserveOperationInput() # ReserveOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_reserve(reserve_operation_input=reserve_operation_input)
        print("The response of AgentsApi->start_agents_reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_operation_input** | [**ReserveOperationInput**](ReserveOperationInput.md)|  | [optional] 

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

# **start_agents_set_dpdk_mode**
> AsyncContext start_agents_set_dpdk_mode(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)



Enable/disable DPDK for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_dpdk_mode_operation_input import SetDpdkModeOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_dpdk_mode_operation_input = kai_inference_builder.SetDpdkModeOperationInput() # SetDpdkModeOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_set_dpdk_mode(set_dpdk_mode_operation_input=set_dpdk_mode_operation_input)
        print("The response of AgentsApi->start_agents_set_dpdk_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_set_dpdk_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_dpdk_mode_operation_input** | [**SetDpdkModeOperationInput**](SetDpdkModeOperationInput.md)|  | [optional] 

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

# **start_agents_set_ntp**
> AsyncContext start_agents_set_ntp(set_ntp_operation_input=set_ntp_operation_input)



Set the NTP servers for a list of agents.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_ntp_operation_input import SetNtpOperationInput
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_ntp_operation_input = kai_inference_builder.SetNtpOperationInput() # SetNtpOperationInput |  (optional)

    try:
        api_response = api_instance.start_agents_set_ntp(set_ntp_operation_input=set_ntp_operation_input)
        print("The response of AgentsApi->start_agents_set_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_set_ntp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ntp_operation_input** | [**SetNtpOperationInput**](SetNtpOperationInput.md)|  | [optional] 

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

# **start_agents_update**
> AsyncContext start_agents_update()



Update agents to the recommended version.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
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
    api_instance = kai_inference_builder.AgentsApi(api_client)

    try:
        api_response = api_instance.start_agents_update()
        print("The response of AgentsApi->start_agents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_agents_update: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AsyncContext**](AsyncContext.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Details about the operation that just started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_controllers_clear_port_ownership**
> AsyncContext start_controllers_clear_port_ownership(clear_ports_ownership_operation=clear_ports_ownership_operation)



Clear the ownership of the ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.clear_ports_ownership_operation import ClearPortsOwnershipOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    clear_ports_ownership_operation = kai_inference_builder.ClearPortsOwnershipOperation() # ClearPortsOwnershipOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_clear_port_ownership(clear_ports_ownership_operation=clear_ports_ownership_operation)
        print("The response of AgentsApi->start_controllers_clear_port_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_clear_port_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_ports_ownership_operation** | [**ClearPortsOwnershipOperation**](ClearPortsOwnershipOperation.md)|  | [optional] 

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

# **start_controllers_power_cycle_nodes**
> AsyncContext start_controllers_power_cycle_nodes(nodes_power_cycle_operation=nodes_power_cycle_operation)



Power cycle the compute nodes.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.nodes_power_cycle_operation import NodesPowerCycleOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    nodes_power_cycle_operation = kai_inference_builder.NodesPowerCycleOperation() # NodesPowerCycleOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_power_cycle_nodes(nodes_power_cycle_operation=nodes_power_cycle_operation)
        print("The response of AgentsApi->start_controllers_power_cycle_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_power_cycle_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodes_power_cycle_operation** | [**NodesPowerCycleOperation**](NodesPowerCycleOperation.md)|  | [optional] 

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

# **start_controllers_reboot_port**
> AsyncContext start_controllers_reboot_port(reboot_ports_operation=reboot_ports_operation)



Reboot ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.reboot_ports_operation import RebootPortsOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    reboot_ports_operation = kai_inference_builder.RebootPortsOperation() # RebootPortsOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_reboot_port(reboot_ports_operation=reboot_ports_operation)
        print("The response of AgentsApi->start_controllers_reboot_port:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_reboot_port: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_ports_operation** | [**RebootPortsOperation**](RebootPortsOperation.md)|  | [optional] 

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

# **start_controllers_set_app**
> AsyncContext start_controllers_set_app(set_controller_app_operation=set_controller_app_operation)



Set the active app of the controllers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_controller_app_operation import SetControllerAppOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_controller_app_operation = kai_inference_builder.SetControllerAppOperation() # SetControllerAppOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_app(set_controller_app_operation=set_controller_app_operation)
        print("The response of AgentsApi->start_controllers_set_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_controller_app_operation** | [**SetControllerAppOperation**](SetControllerAppOperation.md)|  | [optional] 

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

# **start_controllers_set_node_aggregation**
> AsyncContext start_controllers_set_node_aggregation(set_aggregation_mode_operation=set_aggregation_mode_operation)



Set the aggregation mode of the compute nodes.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_aggregation_mode_operation import SetAggregationModeOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_aggregation_mode_operation = kai_inference_builder.SetAggregationModeOperation() # SetAggregationModeOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_node_aggregation(set_aggregation_mode_operation=set_aggregation_mode_operation)
        print("The response of AgentsApi->start_controllers_set_node_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_node_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_aggregation_mode_operation** | [**SetAggregationModeOperation**](SetAggregationModeOperation.md)|  | [optional] 

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

# **start_controllers_set_node_app**
> AsyncContext start_controllers_set_node_app(set_nodes_app_operation=set_nodes_app_operation)



Set the active app of the compute nodes.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_nodes_app_operation import SetNodesAppOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_nodes_app_operation = kai_inference_builder.SetNodesAppOperation() # SetNodesAppOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_node_app(set_nodes_app_operation=set_nodes_app_operation)
        print("The response of AgentsApi->start_controllers_set_node_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_node_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_nodes_app_operation** | [**SetNodesAppOperation**](SetNodesAppOperation.md)|  | [optional] 

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

# **start_controllers_set_port_link_state**
> AsyncContext start_controllers_set_port_link_state(set_ports_link_state_operation=set_ports_link_state_operation)



Set the link state of the ports.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.set_ports_link_state_operation import SetPortsLinkStateOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    set_ports_link_state_operation = kai_inference_builder.SetPortsLinkStateOperation() # SetPortsLinkStateOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_set_port_link_state(set_ports_link_state_operation=set_ports_link_state_operation)
        print("The response of AgentsApi->start_controllers_set_port_link_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_set_port_link_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ports_link_state_operation** | [**SetPortsLinkStateOperation**](SetPortsLinkStateOperation.md)|  | [optional] 

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

# **start_controllers_update_port_tags**
> AsyncContext start_controllers_update_port_tags(update_port_tags_operation=update_port_tags_operation)



Update port tags.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.update_port_tags_operation import UpdatePortTagsOperation
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
    api_instance = kai_inference_builder.AgentsApi(api_client)
    update_port_tags_operation = kai_inference_builder.UpdatePortTagsOperation() # UpdatePortTagsOperation |  (optional)

    try:
        api_response = api_instance.start_controllers_update_port_tags(update_port_tags_operation=update_port_tags_operation)
        print("The response of AgentsApi->start_controllers_update_port_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->start_controllers_update_port_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_port_tags_operation** | [**UpdatePortTagsOperation**](UpdatePortTagsOperation.md)|  | [optional] 

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


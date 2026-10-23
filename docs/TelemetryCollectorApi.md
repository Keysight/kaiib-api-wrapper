# kai_inference_builder.TelemetryCollectorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_telemetry_collector_telemetry_servers**](TelemetryCollectorApi.md#create_telemetry_collector_telemetry_servers) | **POST** /kai-ib/api/v2/telemetry-collector/telemetry-servers | 
[**delete_telemetry_collector_telemetry_server**](TelemetryCollectorApi.md#delete_telemetry_collector_telemetry_server) | **DELETE** /kai-ib/api/v2/telemetry-collector/telemetry-servers/{telemetryServerId} | 
[**get_telemetry_collector_telemetry_server_by_id**](TelemetryCollectorApi.md#get_telemetry_collector_telemetry_server_by_id) | **GET** /kai-ib/api/v2/telemetry-collector/telemetry-servers/{telemetryServerId} | 
[**get_telemetry_collector_telemetry_servers**](TelemetryCollectorApi.md#get_telemetry_collector_telemetry_servers) | **GET** /kai-ib/api/v2/telemetry-collector/telemetry-servers | 
[**patch_telemetry_collector_telemetry_server**](TelemetryCollectorApi.md#patch_telemetry_collector_telemetry_server) | **PATCH** /kai-ib/api/v2/telemetry-collector/telemetry-servers/{telemetryServerId} | 
[**start_telemetry_collector_check_reachability**](TelemetryCollectorApi.md#start_telemetry_collector_check_reachability) | **POST** /kai-ib/api/v2/telemetry-collector/operations/checkReachability | 


# **create_telemetry_collector_telemetry_servers**
> List[TelemetryServerConfig] create_telemetry_collector_telemetry_servers(telemetry_server_config=telemetry_server_config)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.telemetry_server_config import TelemetryServerConfig
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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    telemetry_server_config = [kai_inference_builder.TelemetryServerConfig()] # List[TelemetryServerConfig] |  (optional)

    try:
        api_response = api_instance.create_telemetry_collector_telemetry_servers(telemetry_server_config=telemetry_server_config)
        print("The response of TelemetryCollectorApi->create_telemetry_collector_telemetry_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->create_telemetry_collector_telemetry_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_server_config** | [**List[TelemetryServerConfig]**](TelemetryServerConfig.md)|  | [optional] 

### Return type

[**List[TelemetryServerConfig]**](TelemetryServerConfig.md)

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

# **delete_telemetry_collector_telemetry_server**
> delete_telemetry_collector_telemetry_server(telemetry_server_id)



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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    telemetry_server_id = 'telemetry_server_id_example' # str | The ID of the telemetry server.

    try:
        api_instance.delete_telemetry_collector_telemetry_server(telemetry_server_id)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->delete_telemetry_collector_telemetry_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_server_id** | **str**| The ID of the telemetry server. | 

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

# **get_telemetry_collector_telemetry_server_by_id**
> TelemetryServerConfig get_telemetry_collector_telemetry_server_by_id(telemetry_server_id)



Get a particular telemetry server config.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.telemetry_server_config import TelemetryServerConfig
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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    telemetry_server_id = 'telemetry_server_id_example' # str | The ID of the telemetry server.

    try:
        api_response = api_instance.get_telemetry_collector_telemetry_server_by_id(telemetry_server_id)
        print("The response of TelemetryCollectorApi->get_telemetry_collector_telemetry_server_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->get_telemetry_collector_telemetry_server_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_server_id** | **str**| The ID of the telemetry server. | 

### Return type

[**TelemetryServerConfig**](TelemetryServerConfig.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested telemetry server config |  -  |
**400** | Invalid ID format |  -  |
**404** | A telemetry server config with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telemetry_collector_telemetry_servers**
> GetTelemetryCollectorTelemetryServers200Response get_telemetry_collector_telemetry_servers(take=take, skip=skip)



Get all the configured telemetry servers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_telemetry_collector_telemetry_servers200_response import GetTelemetryCollectorTelemetryServers200Response
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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_telemetry_collector_telemetry_servers(take=take, skip=skip)
        print("The response of TelemetryCollectorApi->get_telemetry_collector_telemetry_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->get_telemetry_collector_telemetry_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetTelemetryCollectorTelemetryServers200Response**](GetTelemetryCollectorTelemetryServers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of telemetry server configs |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_telemetry_collector_telemetry_server**
> patch_telemetry_collector_telemetry_server(telemetry_server_id, telemetry_server_config=telemetry_server_config)



Update a telemetry server config. Only non-empty fields are updated.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.telemetry_server_config import TelemetryServerConfig
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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    telemetry_server_id = 'telemetry_server_id_example' # str | The ID of the telemetry server.
    telemetry_server_config = kai_inference_builder.TelemetryServerConfig() # TelemetryServerConfig |  (optional)

    try:
        api_instance.patch_telemetry_collector_telemetry_server(telemetry_server_id, telemetry_server_config=telemetry_server_config)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->patch_telemetry_collector_telemetry_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_server_id** | **str**| The ID of the telemetry server. | 
 **telemetry_server_config** | [**TelemetryServerConfig**](TelemetryServerConfig.md)|  | [optional] 

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
**200** | The updated telemetry server config |  -  |
**400** | There are no fields to patch. |  -  |
**404** | A telemetry server config with the specified ID was not found. |  -  |
**409** | The new name is already in use, or the new host/port/endpoint matches another server. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_telemetry_collector_check_reachability**
> AsyncContext start_telemetry_collector_check_reachability(reachability_check=reachability_check)



Probe a telemetry server config to check whether the server is reachable

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.reachability_check import ReachabilityCheck
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
    api_instance = kai_inference_builder.TelemetryCollectorApi(api_client)
    reachability_check = [kai_inference_builder.ReachabilityCheck()] # List[ReachabilityCheck] |  (optional)

    try:
        api_response = api_instance.start_telemetry_collector_check_reachability(reachability_check=reachability_check)
        print("The response of TelemetryCollectorApi->start_telemetry_collector_check_reachability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelemetryCollectorApi->start_telemetry_collector_check_reachability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reachability_check** | [**List[ReachabilityCheck]**](ReachabilityCheck.md)|  | [optional] 

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


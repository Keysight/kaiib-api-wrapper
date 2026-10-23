# kai_inference_builder.TestOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_test_run_abort**](TestOperationsApi.md#start_test_run_abort) | **POST** /kai-ib/api/v2/sessions/{sessionId}/test-run/operations/abort | 
[**start_test_run_start**](TestOperationsApi.md#start_test_run_start) | **POST** /kai-ib/api/v2/sessions/{sessionId}/test-run/operations/start | 
[**start_test_run_stop**](TestOperationsApi.md#start_test_run_stop) | **POST** /kai-ib/api/v2/sessions/{sessionId}/test-run/operations/stop | 


# **start_test_run_abort**
> AsyncContext start_test_run_abort(session_id)



Abort traffic for the test configured in the current session.

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
    api_instance = kai_inference_builder.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_test_run_abort(session_id)
        print("The response of TestOperationsApi->start_test_run_abort:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_test_run_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **start_test_run_start**
> AsyncContext start_test_run_start(session_id)



Start traffic for the test configured in the current session.

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
    api_instance = kai_inference_builder.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_test_run_start(session_id)
        print("The response of TestOperationsApi->start_test_run_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_test_run_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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

# **start_test_run_stop**
> AsyncContext start_test_run_stop(session_id)



Stop traffic for the test configured in the current session.

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
    api_instance = kai_inference_builder.TestOperationsApi(api_client)
    session_id = 'session_id_example' # str | The ID of the session.

    try:
        api_response = api_instance.start_test_run_stop(session_id)
        print("The response of TestOperationsApi->start_test_run_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_test_run_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The ID of the session. | 

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


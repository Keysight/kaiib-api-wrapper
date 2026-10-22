# kai_inference_builder.UtilsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_eulas**](UtilsApi.md#check_eulas) | **GET** /eula/v1/check | Check if all EULAs are accepted
[**get_cert_manager_certificate**](UtilsApi.md#get_cert_manager_certificate) | **GET** /kai-ib/api/v2/cert-manager/certificate | 
[**get_disk_usage**](UtilsApi.md#get_disk_usage) | **GET** /kai-ib/api/v2/disk-usage | 
[**get_disk_usage_consumer_by_id**](UtilsApi.md#get_disk_usage_consumer_by_id) | **GET** /kai-ib/api/v2/disk-usage/consumers/{consumerId} | 
[**get_disk_usage_consumers**](UtilsApi.md#get_disk_usage_consumers) | **GET** /kai-ib/api/v2/disk-usage/consumers | 
[**get_eula**](UtilsApi.md#get_eula) | **GET** /eula/v1/eula/{id} | Retrieve EULA detail
[**list_eulas**](UtilsApi.md#list_eulas) | **GET** /eula/v1/eula | list of EULAs
[**post_eula**](UtilsApi.md#post_eula) | **POST** /eula/v1/eula/{id} | Update properties an EULA
[**start_cert_manager_generate**](UtilsApi.md#start_cert_manager_generate) | **POST** /kai-ib/api/v2/cert-manager/operations/generate | 
[**start_cert_manager_upload**](UtilsApi.md#start_cert_manager_upload) | **POST** /kai-ib/api/v2/cert-manager/operations/upload | 
[**start_disk_usage_cleanup_diagnostics**](UtilsApi.md#start_disk_usage_cleanup_diagnostics) | **POST** /kai-ib/api/v2/disk-usage/operations/cleanup-diagnostics | 
[**start_disk_usage_cleanup_logs**](UtilsApi.md#start_disk_usage_cleanup_logs) | **POST** /kai-ib/api/v2/disk-usage/operations/cleanup-logs | 
[**start_disk_usage_cleanup_migration**](UtilsApi.md#start_disk_usage_cleanup_migration) | **POST** /kai-ib/api/v2/disk-usage/operations/cleanup-migration | 
[**start_disk_usage_cleanup_notifications**](UtilsApi.md#start_disk_usage_cleanup_notifications) | **POST** /kai-ib/api/v2/disk-usage/operations/cleanup-notifications | 
[**start_disk_usage_cleanup_results**](UtilsApi.md#start_disk_usage_cleanup_results) | **POST** /kai-ib/api/v2/disk-usage/operations/cleanup-results | 


# **check_eulas**
> check_eulas(x_kcos_eula_bypass=x_kcos_eula_bypass)

Check if all EULAs are accepted

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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    x_kcos_eula_bypass = 'x_kcos_eula_bypass_example' # str |  (optional)

    try:
        # Check if all EULAs are accepted
        api_instance.check_eulas(x_kcos_eula_bypass=x_kcos_eula_bypass)
    except Exception as e:
        print("Exception when calling UtilsApi->check_eulas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_kcos_eula_bypass** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All EULAs are accepted |  -  |
**401** | One or more EULAs are not accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cert_manager_certificate**
> Certificate get_cert_manager_certificate()



Get controller's certificate.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.certificate import Certificate
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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.get_cert_manager_certificate()
        print("The response of UtilsApi->get_cert_manager_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_cert_manager_certificate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Certificate**](Certificate.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The controller&#39;s certificate |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_usage**
> DiskUsage get_disk_usage()



Get information about the controller's disk usage.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.disk_usage import DiskUsage
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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.get_disk_usage()
        print("The response of UtilsApi->get_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_disk_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DiskUsage**](DiskUsage.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The controller disk usage |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_usage_consumer_by_id**
> Consumer get_disk_usage_consumer_by_id(consumer_id)



Get the size for logs and diagnostics.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.consumer import Consumer
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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    consumer_id = 'consumer_id_example' # str | The ID of the consumer.

    try:
        api_response = api_instance.get_disk_usage_consumer_by_id(consumer_id)
        print("The response of UtilsApi->get_disk_usage_consumer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_disk_usage_consumer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| The ID of the consumer. | 

### Return type

[**Consumer**](Consumer.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about logs and diagnostics size |  -  |
**400** | Bad request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_usage_consumers**
> GetDiskUsageConsumers200Response get_disk_usage_consumers(take=take, skip=skip)



Get the list of consumers.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_disk_usage_consumers200_response import GetDiskUsageConsumers200Response
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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_disk_usage_consumers(take=take, skip=skip)
        print("The response of UtilsApi->get_disk_usage_consumers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_disk_usage_consumers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetDiskUsageConsumers200Response**](GetDiskUsageConsumers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of consumers which can be either logs or diagnostics |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eula**
> EulaDetails get_eula(id)

Retrieve EULA detail

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.eula_details import EulaDetails
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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    id = 'id_example' # str | The ID of the EULA.

    try:
        # Retrieve EULA detail
        api_response = api_instance.get_eula(id)
        print("The response of UtilsApi->get_eula:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_eula: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the EULA. | 

### Return type

[**EulaDetails**](EulaDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | EULA not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_eulas**
> List[EulaSummary] list_eulas()

list of EULAs

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.eula_summary import EulaSummary
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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        # list of EULAs
        api_response = api_instance.list_eulas()
        print("The response of UtilsApi->list_eulas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->list_eulas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EulaSummary]**](EulaSummary.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_eula**
> str post_eula(id, eula_summary=eula_summary)

Update properties an EULA

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.eula_summary import EulaSummary
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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    id = 'id_example' # str | The ID of the EULA.
    eula_summary = kai_inference_builder.EulaSummary() # EulaSummary |  (optional)

    try:
        # Update properties an EULA
        api_response = api_instance.post_eula(id, eula_summary=eula_summary)
        print("The response of UtilsApi->post_eula:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->post_eula: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the EULA. | 
 **eula_summary** | [**EulaSummary**](EulaSummary.md)|  | [optional] 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | EULA not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_cert_manager_generate**
> AsyncContext start_cert_manager_generate(certificate=certificate)



Generate a certificate.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.certificate import Certificate
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
    api_instance = kai_inference_builder.UtilsApi(api_client)
    certificate = kai_inference_builder.Certificate() # Certificate |  (optional)

    try:
        api_response = api_instance.start_cert_manager_generate(certificate=certificate)
        print("The response of UtilsApi->start_cert_manager_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_cert_manager_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**Certificate**](Certificate.md)|  | [optional] 

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

# **start_cert_manager_upload**
> AsyncContext start_cert_manager_upload()



Upload a certificate/key pair that will replace the system certificate.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_cert_manager_upload()
        print("The response of UtilsApi->start_cert_manager_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_cert_manager_upload: %s\n" % e)
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

# **start_disk_usage_cleanup_diagnostics**
> AsyncContext start_disk_usage_cleanup_diagnostics()



Clean the system diagnostics.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_disk_usage_cleanup_diagnostics()
        print("The response of UtilsApi->start_disk_usage_cleanup_diagnostics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_disk_usage_cleanup_diagnostics: %s\n" % e)
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

# **start_disk_usage_cleanup_logs**
> AsyncContext start_disk_usage_cleanup_logs()



Clean the system logs.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_disk_usage_cleanup_logs()
        print("The response of UtilsApi->start_disk_usage_cleanup_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_disk_usage_cleanup_logs: %s\n" % e)
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

# **start_disk_usage_cleanup_migration**
> AsyncContext start_disk_usage_cleanup_migration()



Clean the migration packages.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_disk_usage_cleanup_migration()
        print("The response of UtilsApi->start_disk_usage_cleanup_migration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_disk_usage_cleanup_migration: %s\n" % e)
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

# **start_disk_usage_cleanup_notifications**
> AsyncContext start_disk_usage_cleanup_notifications()



Clean all notifications.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_disk_usage_cleanup_notifications()
        print("The response of UtilsApi->start_disk_usage_cleanup_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_disk_usage_cleanup_notifications: %s\n" % e)
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

# **start_disk_usage_cleanup_results**
> AsyncContext start_disk_usage_cleanup_results()



Clean all statistics.

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
    api_instance = kai_inference_builder.UtilsApi(api_client)

    try:
        api_response = api_instance.start_disk_usage_cleanup_results()
        print("The response of UtilsApi->start_disk_usage_cleanup_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->start_disk_usage_cleanup_results: %s\n" % e)
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


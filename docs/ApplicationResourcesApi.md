# kai_inference_builder.ApplicationResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resources_profile_by_id**](ApplicationResourcesApi.md#get_resources_profile_by_id) | **GET** /kai-ib/api/v2/resources/profiles/{profileId} | 
[**get_resources_profile_icon**](ApplicationResourcesApi.md#get_resources_profile_icon) | **GET** /kai-ib/api/v2/resources/profiles/{profileId}/icon | 
[**get_resources_profile_topology_img**](ApplicationResourcesApi.md#get_resources_profile_topology_img) | **GET** /kai-ib/api/v2/resources/profiles/{profileId}/topologyImg | 
[**get_resources_profiles**](ApplicationResourcesApi.md#get_resources_profiles) | **GET** /kai-ib/api/v2/resources/profiles | 
[**get_resources_sub_profile_by_id**](ApplicationResourcesApi.md#get_resources_sub_profile_by_id) | **GET** /kai-ib/api/v2/resources/sub-profiles/{subProfileId} | 
[**get_resources_sub_profile_categories**](ApplicationResourcesApi.md#get_resources_sub_profile_categories) | **GET** /kai-ib/api/v2/resources/sub-profile-categories | 
[**get_resources_sub_profiles**](ApplicationResourcesApi.md#get_resources_sub_profiles) | **GET** /kai-ib/api/v2/resources/sub-profiles | 
[**get_sub_profile_formatted_description**](ApplicationResourcesApi.md#get_sub_profile_formatted_description) | **GET** /kai-ib/api/v2/resources/sub-profiles/{subProfileId}/formattedDescription | 
[**get_sub_profile_keywords**](ApplicationResourcesApi.md#get_sub_profile_keywords) | **GET** /kai-ib/api/v2/resources/sub-profiles/{subProfileId}/keywords | 
[**start_resources_get_sub_profile_categories**](ApplicationResourcesApi.md#start_resources_get_sub_profile_categories) | **POST** /kai-ib/api/v2/resources/operations/get-sub-profile-categories | 
[**start_resources_get_sub_profiles**](ApplicationResourcesApi.md#start_resources_get_sub_profiles) | **POST** /kai-ib/api/v2/resources/operations/get-sub-profiles | 
[**start_resources_sub_profile_modify_excluded_dut_recursively**](ApplicationResourcesApi.md#start_resources_sub_profile_modify_excluded_dut_recursively) | **POST** /kai-ib/api/v2/resources/sub-profiles/{subProfileId}/operations/modify-excluded-dut-recursively | 
[**start_resources_sub_profile_modify_tags_recursively**](ApplicationResourcesApi.md#start_resources_sub_profile_modify_tags_recursively) | **POST** /kai-ib/api/v2/resources/sub-profiles/{subProfileId}/operations/modify-tags-recursively | 


# **get_resources_profile_by_id**
> Profile get_resources_profile_by_id(profile_id)



Get a particular profile.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.profile import Profile
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile.

    try:
        api_response = api_instance.get_resources_profile_by_id(profile_id)
        print("The response of ApplicationResourcesApi->get_resources_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile. | 

### Return type

[**Profile**](Profile.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested profile |  -  |
**404** | A profile with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_profile_icon**
> get_resources_profile_icon(profile_id)



Get the icon image of a particular profile.

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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile.

    try:
        api_instance.get_resources_profile_icon(profile_id)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_profile_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile. | 

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
**200** | The icon image bytes |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | A profile with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_profile_topology_img**
> get_resources_profile_topology_img(profile_id, theme=theme)



Get the topology image of a particular profile.

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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile.
    theme = 'theme_example' # str | Image theme: light (default) or dark (optional)

    try:
        api_instance.get_resources_profile_topology_img(profile_id, theme=theme)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_profile_topology_img: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile. | 
 **theme** | **str**| Image theme: light (default) or dark | [optional] 

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
**200** | The topology image bytes |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | A profile with the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_profiles**
> GetResourcesProfiles200Response get_resources_profiles(take=take, skip=skip)



Get all the available profiles.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_resources_profiles200_response import GetResourcesProfiles200Response
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_resources_profiles(take=take, skip=skip)
        print("The response of ApplicationResourcesApi->get_resources_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetResourcesProfiles200Response**](GetResourcesProfiles200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of profiles |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_sub_profile_by_id**
> SubProfile get_resources_sub_profile_by_id(sub_profile_id)



Get a particular sub-profile.

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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the sub profile.

    try:
        api_response = api_instance.get_resources_sub_profile_by_id(sub_profile_id)
        print("The response of ApplicationResourcesApi->get_resources_sub_profile_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_sub_profile_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_profile_id** | **str**| The ID of the sub profile. | 

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
**200** | The requested sub-profile |  -  |
**404** | A sub-profile with the specified ID was not found. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_sub_profile_categories**
> List[Category] get_resources_sub_profile_categories(take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.category import Category
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_resources_sub_profile_categories(take=take, skip=skip)
        print("The response of ApplicationResourcesApi->get_resources_sub_profile_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_sub_profile_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Category]**](Category.md)

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

# **get_resources_sub_profiles**
> GetResourcesSubProfiles200Response get_resources_sub_profiles(take=take, skip=skip)



Get all the available sub-profiles.

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.get_resources_sub_profiles200_response import GetResourcesSubProfiles200Response
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_resources_sub_profiles(take=take, skip=skip)
        print("The response of ApplicationResourcesApi->get_resources_sub_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_resources_sub_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**GetResourcesSubProfiles200Response**](GetResourcesSubProfiles200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of sub-profiles |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_profile_formatted_description**
> FormattedDescription get_sub_profile_formatted_description(sub_profile_id)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.formatted_description import FormattedDescription
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the sub profile.

    try:
        api_response = api_instance.get_sub_profile_formatted_description(sub_profile_id)
        print("The response of ApplicationResourcesApi->get_sub_profile_formatted_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_sub_profile_formatted_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_profile_id** | **str**| The ID of the sub profile. | 

### Return type

[**FormattedDescription**](FormattedDescription.md)

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

# **get_sub_profile_keywords**
> List[Keyword] get_sub_profile_keywords(sub_profile_id, take=take, skip=skip)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.keyword import Keyword
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the sub profile.
    take = 56 # int | The number of search results to return (optional)
    skip = 56 # int | The number of search results to skip (optional)

    try:
        api_response = api_instance.get_sub_profile_keywords(sub_profile_id, take=take, skip=skip)
        print("The response of ApplicationResourcesApi->get_sub_profile_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->get_sub_profile_keywords: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_profile_id** | **str**| The ID of the sub profile. | 
 **take** | **int**| The number of search results to return | [optional] 
 **skip** | **int**| The number of search results to skip | [optional] 

### Return type

[**List[Keyword]**](Keyword.md)

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

# **start_resources_get_sub_profile_categories**
> AsyncContext start_resources_get_sub_profile_categories(get_categories_operation=get_categories_operation)



Get the list of sub-profile categories

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.get_categories_operation import GetCategoriesOperation
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    get_categories_operation = kai_inference_builder.GetCategoriesOperation() # GetCategoriesOperation |  (optional)

    try:
        api_response = api_instance.start_resources_get_sub_profile_categories(get_categories_operation=get_categories_operation)
        print("The response of ApplicationResourcesApi->start_resources_get_sub_profile_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->start_resources_get_sub_profile_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_categories_operation** | [**GetCategoriesOperation**](GetCategoriesOperation.md)|  | [optional] 

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

# **start_resources_get_sub_profiles**
> AsyncContext start_resources_get_sub_profiles(get_scenarios_operation=get_scenarios_operation)



Get the list of sub-profiles

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.get_scenarios_operation import GetScenariosOperation
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    get_scenarios_operation = kai_inference_builder.GetScenariosOperation() # GetScenariosOperation |  (optional)

    try:
        api_response = api_instance.start_resources_get_sub_profiles(get_scenarios_operation=get_scenarios_operation)
        print("The response of ApplicationResourcesApi->start_resources_get_sub_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->start_resources_get_sub_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scenarios_operation** | [**GetScenariosOperation**](GetScenariosOperation.md)|  | [optional] 

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

# **start_resources_sub_profile_modify_excluded_dut_recursively**
> AsyncContext start_resources_sub_profile_modify_excluded_dut_recursively(sub_profile_id, update_network_mapping=update_network_mapping)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.update_network_mapping import UpdateNetworkMapping
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the sub profile.
    update_network_mapping = kai_inference_builder.UpdateNetworkMapping() # UpdateNetworkMapping |  (optional)

    try:
        api_response = api_instance.start_resources_sub_profile_modify_excluded_dut_recursively(sub_profile_id, update_network_mapping=update_network_mapping)
        print("The response of ApplicationResourcesApi->start_resources_sub_profile_modify_excluded_dut_recursively:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->start_resources_sub_profile_modify_excluded_dut_recursively: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_profile_id** | **str**| The ID of the sub profile. | 
 **update_network_mapping** | [**UpdateNetworkMapping**](UpdateNetworkMapping.md)|  | [optional] 

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

# **start_resources_sub_profile_modify_tags_recursively**
> AsyncContext start_resources_sub_profile_modify_tags_recursively(sub_profile_id, update_network_mapping=update_network_mapping)



### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import kai_inference_builder
from kai_inference_builder.models.async_context import AsyncContext
from kai_inference_builder.models.update_network_mapping import UpdateNetworkMapping
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
    api_instance = kai_inference_builder.ApplicationResourcesApi(api_client)
    sub_profile_id = 'sub_profile_id_example' # str | The ID of the sub profile.
    update_network_mapping = kai_inference_builder.UpdateNetworkMapping() # UpdateNetworkMapping |  (optional)

    try:
        api_response = api_instance.start_resources_sub_profile_modify_tags_recursively(sub_profile_id, update_network_mapping=update_network_mapping)
        print("The response of ApplicationResourcesApi->start_resources_sub_profile_modify_tags_recursively:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationResourcesApi->start_resources_sub_profile_modify_tags_recursively: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_profile_id** | **str**| The ID of the sub profile. | 
 **update_network_mapping** | [**UpdateNetworkMapping**](UpdateNetworkMapping.md)|  | [optional] 

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


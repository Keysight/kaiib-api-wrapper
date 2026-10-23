# SubProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_timeout** | **int** | The action timeout value of the Scenario. | [optional] 
**active** | **bool** | Indicates whether the scenario is enabled or not. | [optional] 
**client_http_profile** | [**HTTPProfile**](HTTPProfile.md) |  | [optional] 
**client_quic_profile** | [**QUICProfile**](QUICProfile.md) |  | [optional] 
**client_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**connections_max_transactions** | **int** | The maximum number of transactions for all scenario connections. | [optional] 
**data_types** | [**List[DataType]**](DataType.md) |  | [optional] 
**description** | **str** | The description of the Scenario. | [optional] 
**destination_hostname** | **str** |  | [optional] 
**dnn_id** | **str** |  | [optional] 
**end_point_id** | **int** | The endpoint ID of the Scenario. | [optional] 
**endpoints** | [**List[Endpoint]**](Endpoint.md) |  | [optional] [readonly] 
**external_resource_url** | **str** | The external resource URL of the Scenario. | [optional] 
**index** | **int** | The index of the scenario. | [optional] [readonly] 
**inherit_http_profile** | **bool** |  | [optional] 
**inherit_llmapi** | **bool** |  | [optional] 
**inherit_quic_profile** | **bool** |  | [optional] 
**inherit_tls** | **bool** |  | [optional] 
**ip_preference** | [**IpPreference**](IpPreference.md) |  | [optional] 
**is_deprecated** | **bool** | A value that indicates if the action is deprecated. | [optional] [readonly] 
**is_stateless_stream** | **bool** |  | [optional] [readonly] 
**is_streaming** | **bool** |  | [optional] [readonly] 
**iteration_count** | **int** | The iteration counter of the Scenario. | [optional] 
**llmapi_profiles** | [**List[LLMAPIProfile]**](LLMAPIProfile.md) |  | [optional] 
**max_active_limit** | **int** | The maximum active limit of the Scenario. | [optional] 
**name** | **str** |  | [optional] 
**network_mapping** | [**NetworkMapping**](NetworkMapping.md) |  | [optional] 
**objective_weight** | **int** | The objective weight of the application. | [optional] 
**params** | [**List[Params]**](Params.md) |  | [optional] 
**protocol_found** | **bool** |  | [optional] [readonly] 
**protocol_id** | **str** | The protocol ID of the Scenario. | [optional] 
**qos_flow_id** | **str** |  | [optional] 
**readonly_max_trans** | **bool** | If true, ConnectionsMaxTransactions will be readonly. | [optional] [readonly] 
**server_http_profile** | [**HTTPProfile**](HTTPProfile.md) |  | [optional] 
**server_quic_profile** | [**QUICProfile**](QUICProfile.md) |  | [optional] 
**server_tls_profile** | [**TLSProfile**](TLSProfile.md) |  | [optional] 
**stateless_stream** | [**StatelessStream**](StatelessStream.md) |  | [optional] 
**static** | **bool** |  | [optional] [readonly] 
**supported_apps** | **List[str]** |  | [optional] 
**supports_calibration** | **bool** |  | [optional] [readonly] 
**supports_client_http_profile** | **bool** | Indicates if the scenario supports Client HTTP profile. | [optional] 
**supports_http2** | **bool** |  | [optional] [readonly] 
**supports_http_profiles** | **bool** | Indicates if the scenario supports HTTP profiles. | [optional] 
**supports_multi_flow** | **bool** |  | [optional] [readonly] 
**supports_server_http_profile** | **bool** | Indicates if the scenario supports Server HTTP profile. | [optional] 
**supports_strikes** | **bool** |  | [optional] [readonly] 
**supports_tls** | **bool** |  | [optional] [readonly] 
**tracks** | [**List[Track]**](Track.md) |  | [optional] 
**action_timeout** | **int** | The action timeout value in seconds of the SubProfile. | [optional] 
**formatted_description** | [**FormattedDescription**](FormattedDescription.md) |  | [optional] 
**id** | **str** |  | [optional] 
**keywords** | [**List[Keyword]**](Keyword.md) | The aggregated keywords of the sub-profile | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the sub-profile. | [optional] 
**objective_weight** | **int** | The objective weight of the SubProfile. | [optional] 
**owner** | **str** | The friendly display name of the sub-profile&#39;s owner | [optional] [readonly] 
**owner_id** | **str** | The unique identifier of the sub-profile&#39;s owner | [optional] [readonly] 
**resource_id** | **str** | The resource ID of the SubProfile. | [optional] [readonly] 

## Example

```python
from kai_inference_builder.models.sub_profile import SubProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SubProfile from a JSON string
sub_profile_instance = SubProfile.from_json(json)
# print the JSON string representation of the object
print(SubProfile.to_json())

# convert the object into a dict
sub_profile_dict = sub_profile_instance.to_dict()
# create an instance of SubProfile from a dict
sub_profile_from_dict = SubProfile.from_dict(sub_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



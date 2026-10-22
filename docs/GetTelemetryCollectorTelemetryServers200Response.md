# GetTelemetryCollectorTelemetryServers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TelemetryServerConfig]**](TelemetryServerConfig.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from kai_inference_builder.models.get_telemetry_collector_telemetry_servers200_response import GetTelemetryCollectorTelemetryServers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTelemetryCollectorTelemetryServers200Response from a JSON string
get_telemetry_collector_telemetry_servers200_response_instance = GetTelemetryCollectorTelemetryServers200Response.from_json(json)
# print the JSON string representation of the object
print(GetTelemetryCollectorTelemetryServers200Response.to_json())

# convert the object into a dict
get_telemetry_collector_telemetry_servers200_response_dict = get_telemetry_collector_telemetry_servers200_response_instance.to_dict()
# create an instance of GetTelemetryCollectorTelemetryServers200Response from a dict
get_telemetry_collector_telemetry_servers200_response_from_dict = GetTelemetryCollectorTelemetryServers200Response.from_dict(get_telemetry_collector_telemetry_servers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



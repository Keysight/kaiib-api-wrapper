# TelemetryServerConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_url** | **str** | Path of the metrics endpoint | [optional] 
**host** | **str** | Hostname or IP address of the telemetry server | [optional] 
**id** | **str** | The unique identifier of the telemetry server configuration | [optional] [readonly] 
**name** | **str** | Name of the Telemetry Server Config | [optional] 
**port** | **str** | Port where telemetry metrics are exposed | [optional] 
**reference_links** | **Dict[str, int]** |  | [optional] 

## Example

```python
from kai_inference_builder.models.telemetry_server_config import TelemetryServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetryServerConfig from a JSON string
telemetry_server_config_instance = TelemetryServerConfig.from_json(json)
# print the JSON string representation of the object
print(TelemetryServerConfig.to_json())

# convert the object into a dict
telemetry_server_config_dict = telemetry_server_config_instance.to_dict()
# create an instance of TelemetryServerConfig from a dict
telemetry_server_config_from_dict = TelemetryServerConfig.from_dict(telemetry_server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



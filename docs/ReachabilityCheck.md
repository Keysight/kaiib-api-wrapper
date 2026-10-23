# ReachabilityCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Details about the reachability of the server. Unreachable errors or warnings for a reachable server | [optional] [readonly] 
**reachable** | **bool** | True if the telemetry server answered the probe | [optional] [readonly] 
**server_config** | [**TelemetryServerConfig**](TelemetryServerConfig.md) |  | [optional] 
**server_config_id** | **str** | The ID of the stored telemetry server config to probe. This value can be omitted if a serverConfig is specified, and it will be prioritized over the serverConfig if both are provided. | [optional] 

## Example

```python
from kai_inference_builder.models.reachability_check import ReachabilityCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ReachabilityCheck from a JSON string
reachability_check_instance = ReachabilityCheck.from_json(json)
# print the JSON string representation of the object
print(ReachabilityCheck.to_json())

# convert the object into a dict
reachability_check_dict = reachability_check_instance.to_dict()
# create an instance of ReachabilityCheck from a dict
reachability_check_from_dict = ReachabilityCheck.from_dict(reachability_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



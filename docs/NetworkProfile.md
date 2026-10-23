# NetworkProfile

The networks assigned to the current test configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dut_network_segment** | [**List[DUTNetwork]**](DUTNetwork.md) |  | [optional] 
**ip_network_segment** | [**List[IPNetwork]**](IPNetwork.md) |  | [optional] 
**duts** | [**List[Dut]**](Dut.md) | The Devices Under Test configured for the test. | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**networks** | [**List[Network]**](Network.md) | The network segments configured for the test. | [optional] 
**telemetry_server_ids** | **List[str]** | The telemetry servers configured for the test. | [optional] 

## Example

```python
from kai_inference_builder.models.network_profile import NetworkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkProfile from a JSON string
network_profile_instance = NetworkProfile.from_json(json)
# print the JSON string representation of the object
print(NetworkProfile.to_json())

# convert the object into a dict
network_profile_dict = network_profile_instance.to_dict()
# create an instance of NetworkProfile from a dict
network_profile_from_dict = NetworkProfile.from_dict(network_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



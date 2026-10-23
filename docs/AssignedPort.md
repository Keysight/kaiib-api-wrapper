# AssignedPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_settings** | [**CaptureSettings**](CaptureSettings.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**port_id** | **str** | The id of the port that is assigned. | [optional] 

## Example

```python
from kai_inference_builder.models.assigned_port import AssignedPort

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedPort from a JSON string
assigned_port_instance = AssignedPort.from_json(json)
# print the JSON string representation of the object
print(AssignedPort.to_json())

# convert the object into a dict
assigned_port_dict = assigned_port_instance.to_dict()
# create an instance of AssignedPort from a dict
assigned_port_from_dict = AssignedPort.from_dict(assigned_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



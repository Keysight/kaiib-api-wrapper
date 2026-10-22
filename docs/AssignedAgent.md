# AssignedAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | The id of the agent that is assigned. | [optional] 
**capture_settings** | [**CaptureSettings**](CaptureSettings.md) |  | [optional] 
**id** | **str** |  | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from kai_inference_builder.models.assigned_agent import AssignedAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedAgent from a JSON string
assigned_agent_instance = AssignedAgent.from_json(json)
# print the JSON string representation of the object
print(AssignedAgent.to_json())

# convert the object into a dict
assigned_agent_dict = assigned_agent_instance.to_dict()
# create an instance of AssignedAgent from a dict
assigned_agent_from_dict = AssignedAgent.from_dict(assigned_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



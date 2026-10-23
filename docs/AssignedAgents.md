# AssignedAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[AssignedAgent]**](AssignedAgent.md) | The agents statically assigned to the current test configuration. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**ports** | [**List[AssignedPort]**](AssignedPort.md) | The ports assigned to the current test configuration. | [optional] 

## Example

```python
from kai_inference_builder.models.assigned_agents import AssignedAgents

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedAgents from a JSON string
assigned_agents_instance = AssignedAgents.from_json(json)
# print the JSON string representation of the object
print(AssignedAgents.to_json())

# convert the object into a dict
assigned_agents_dict = assigned_agents_instance.to_dict()
# create an instance of AssignedAgents from a dict
assigned_agents_from_dict = AssignedAgents.from_dict(assigned_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



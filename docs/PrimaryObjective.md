# PrimaryObjective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | The duration of the test run (default: 600). | [optional] 
**objective_value** | **float** | The value of the primary objective. | [optional] 
**type** | **str** | The type of primary objective (Prompts per second). | [optional] 

## Example

```python
from kai_inference_builder.models.primary_objective import PrimaryObjective

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryObjective from a JSON string
primary_objective_instance = PrimaryObjective.from_json(json)
# print the JSON string representation of the object
print(PrimaryObjective.to_json())

# convert the object into a dict
primary_objective_dict = primary_objective_instance.to_dict()
# create an instance of PrimaryObjective from a dict
primary_objective_from_dict = PrimaryObjective.from_dict(primary_objective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



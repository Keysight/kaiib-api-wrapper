# SaveConfigOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**overwrite** | **bool** |  | [optional] 
**skip_session_patch** | **bool** |  | [optional] 

## Example

```python
from kai_inference_builder.models.save_config_operation import SaveConfigOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfigOperation from a JSON string
save_config_operation_instance = SaveConfigOperation.from_json(json)
# print the JSON string representation of the object
print(SaveConfigOperation.to_json())

# convert the object into a dict
save_config_operation_dict = save_config_operation_instance.to_dict()
# create an instance of SaveConfigOperation from a dict
save_config_operation_from_dict = SaveConfigOperation.from_dict(save_config_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



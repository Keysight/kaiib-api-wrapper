# AddSubProfilesOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The resource IDs of the sub-profiles to add to the session. | [optional] 

## Example

```python
from kai_inference_builder.models.add_sub_profiles_operation import AddSubProfilesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AddSubProfilesOperation from a JSON string
add_sub_profiles_operation_instance = AddSubProfilesOperation.from_json(json)
# print the JSON string representation of the object
print(AddSubProfilesOperation.to_json())

# convert the object into a dict
add_sub_profiles_operation_dict = add_sub_profiles_operation_instance.to_dict()
# create an instance of AddSubProfilesOperation from a dict
add_sub_profiles_operation_from_dict = AddSubProfilesOperation.from_dict(add_sub_profiles_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



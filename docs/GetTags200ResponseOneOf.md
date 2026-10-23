# GetTags200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgentsGroup]**](AgentsGroup.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from kai_inference_builder.models.get_tags200_response_one_of import GetTags200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetTags200ResponseOneOf from a JSON string
get_tags200_response_one_of_instance = GetTags200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetTags200ResponseOneOf.to_json())

# convert the object into a dict
get_tags200_response_one_of_dict = get_tags200_response_one_of_instance.to_dict()
# create an instance of GetTags200ResponseOneOf from a dict
get_tags200_response_one_of_from_dict = GetTags200ResponseOneOf.from_dict(get_tags200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



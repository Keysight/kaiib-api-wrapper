# KAIIBConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the KAI IB configuration | [optional] [readonly] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 
**name** | **str** | The name of the configuration | [optional] 
**network_profile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**objectives_and_timeline** | [**ObjectivesAndTimeline**](ObjectivesAndTimeline.md) |  | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**session_id** | **str** | The unique identifier of the session this configuration belongs to | [optional] [readonly] 
**sub_profiles** | [**List[SubProfile]**](SubProfile.md) | The list of sub-profiles configured for this session. | [optional] 
**template_id** | **str** | The unique identifier of the template that wraps this config | [optional] [readonly] 

## Example

```python
from kai_inference_builder.models.kaiib_config import KAIIBConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KAIIBConfig from a JSON string
kaiib_config_instance = KAIIBConfig.from_json(json)
# print the JSON string representation of the object
print(KAIIBConfig.to_json())

# convert the object into a dict
kaiib_config_dict = kaiib_config_instance.to_dict()
# create an instance of KAIIBConfig from a dict
kaiib_config_from_dict = KAIIBConfig.from_dict(kaiib_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



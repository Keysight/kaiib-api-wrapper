# Dut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**model** | **str** | The identifier of the LLM model to use for inference. | [optional] 
**request_url_host** | **str** | The IP or hostname of the DUT to use for inference. | [optional] 
**request_url_path** | **str** | The endpoint URL for the LLM chat completions API. | [optional] 
**request_url_port** | **int** | The port of the DUT to use for inference. | [optional] 

## Example

```python
from kai_inference_builder.models.dut import Dut

# TODO update the JSON string below
json = "{}"
# create an instance of Dut from a JSON string
dut_instance = Dut.from_json(json)
# print the JSON string representation of the object
print(Dut.to_json())

# convert the object into a dict
dut_dict = dut_instance.to_dict()
# create an instance of Dut from a dict
dut_from_dict = Dut.from_dict(dut_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



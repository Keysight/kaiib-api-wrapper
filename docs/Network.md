# Network


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_agents** | [**AssignedAgents**](AssignedAgents.md) |  | [optional] 
**dns_resolver** | [**DNSResolver**](DNSResolver.md) |  | [optional] 
**id** | **str** |  | [optional] 
**ip_ranges** | [**List[IPRange]**](IPRange.md) | The IP ranges assigned to this network segment. | [optional] 
**links** | [**List[APILink]**](APILink.md) |  | [optional] 

## Example

```python
from kai_inference_builder.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_from_dict = Network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



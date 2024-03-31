"""
NOTE: This is under construction. DO NOT USE.
"""

import json 
import requests 

bridge_url = "https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews"
bridge_params = {
  "access_token": "55f40e59f06d606b429bea23cd76b81a",
}

response = requests.request("GET",bridge_url, params=bridge_params)
print(response.text)

"""
class ZillowClient:
"""
"""
    def __init__(self):
"""

"""
  SKIP lets you skip past the input # of items.
  SELECT lets you select viable properties (OfficeType)
  UNSELECT lets you remove viable properties.
  TOP shows the input # of items at the top of the list.
  ORDERBY allows you to ordered by the input property values.
  
  def get_reviews(iSkip, iSelect, iUnselect,iTop,iOrderby):
    url = https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews?access_token=55f40e59f06d606b429bea23cd76b81a&$skip={iSkip}&$select={iSelect}&$unselect={iUnselect}&$top={iTop}&$orderby={iOrderby}
"""


"""
https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews?access_token=55f40e59f06d606b429bea23cd76b81a&$skip=80&$select=applea&$unselect=arnahl&$top=deedee&$orderby=42
"""
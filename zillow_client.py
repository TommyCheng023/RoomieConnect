"""
NOTE: This is under construction. DO NOT USE.
"""

import json 
import requests 

class ZillowClient:
  def __init__(self):
    self.review_url = "https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews" 

    
"""
NOTE: If you don't want to use all of the params, type None as input.
"""
def get_reviews(self,iUrl, iSkip,iSelect,iUnselect,iTop,iOrderby):
  bridge_url = iUrl
  bridge_params = {
    "access_token": "55f40e59f06d606b429bea23cd76b81a",
    "$skip": iSkip, 
    "$select": iSelect,
    "$unselect":iUnselect,
    "$top":iTop,
    "$orderby":iOrderby
  }

  response = requests.request("GET",bridge_url, params=bridge_params)
  if response.ok():
    print(response.text)
    return response.json()
  else:
    response.raise_for_status()
"""


bridge_url = "https://api.bridgedataoutput.com/api/v2/OData/reviews/Reviews"
bridge_params = {
  "access_token": "55f40e59f06d606b429bea23cd76b81a",
  "$skip":84,
  "$select": None

}

response = requests.get(bridge_url, params=bridge_params)
print(response.text)
"""
  


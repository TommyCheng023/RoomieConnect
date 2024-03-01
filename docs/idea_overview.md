## Idea One
Our first idea is **Off-campus Roommates Marketplace**, which is going to be a web app helping students who live off-campus finding their ideal roommates by matching information of `age`, `grade classification`, `building preference`, `rent budget` and so on. 
* app name: **RoomieConnect**
* users' profile information is collected and stored in a database (`MySQL`)
* popular off-campus building statistics: apartment.com, [Zillow](https://www.zillow.com/research/data/)
```sh
# apartment.com
GET https://api.apartments.com/v1/api/reviews?pageSize=100&pageNumber=1
Authorization: Bearer <TOKEN>
Accept: application/json

HTTP/1.1 200 OK
{
  "ReviewCount": 1,
  "CurrentPage": 1,
  "TotalPages": 1,
  "Reviews": [
    {
      "ReviewId": 1234,
      "CultureCode": "en-us",
      "Title": "I love this place!",
      "Text": "I have live here for 2 years now and...",
      "Rating": 4
    }
  ]
}
```
* personal authentication: Google Sign In (BU email restriction)
* decoupled architecture: Flask for backend and HTML with Jinja Template for frontend

## Idea Two
Our second idea is a **traveling app**, which is going to make a quick introduction of the country
* 
* popu

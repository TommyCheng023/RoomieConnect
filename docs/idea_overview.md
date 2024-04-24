## Idea One
Our first idea is **Off-campus Roommates Marketplace**, which is going to be a web app helping students who live off-campus finding their ideal roommates by matching information of `age`, `grade classification`, `building preference`, `rent budget` and so on. 
* app name: **RoomieConnect**
* users' profile information is collected and stored in a database (`MySQL`)
* API choices
  * popular off-campus building statistics: [Zillow](https://www.zillow.com/research/data/), [Yotpo](https://core-api.yotpo.com/reference/welcome#)
* personal authentication: Google Sign In (BU email restriction)
* decoupled architecture: `Flask` for backend and `HTML with Jinja Template` for frontend

## Idea Two
Our second idea is a **traveling app**, which is going to make a quick introduction of the country the client is planning to travel to, including the `location`, `famous scenic spots`, `travel budget` and so on. 
* app name: **WonderSphere**
* users' profile information is collected and stored in a database (`MySQL`)
* API choices
  * [`WeatherStack`](https://weatherstack.com/usage): real-time weather forecasting
  * [`REST Countries`](https://restcountries.com/): offer countries' detailed information
* personal authentication: Google Sign In (gmail)
* decoupled architecture: `Next.js`

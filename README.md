# CS-411-Group-Project
* Planned Project Framework: Flask + Jinja + MySQL

### Each person needs to create an individual local branch and work on the branch. **Don't push directly on master!**

# Environment Setup
```sh
pip install -r requirements.txt
```

# Database Setup:
* Please install [MySQL](https://www.mysql.com/products/workbench/) first !!!
* After installing MySQL, please update your own Config.py, unless you are using the default setting.

```sh
python initialize_db.py
```
# Project Overview
### Demo
* Since GitHub does not accept adding files over 100MB, this demo is too short to display all implemented page logic.
   * **examples:** auto logout due to session expiration; registration/update profile restriction rules; dynamic templates for profile and roommate pages; abnormal session detection

https://github.com/TommyCheng023/CS-411-Group-Project/assets/115842289/5bf57e59-8ce7-4524-b180-a5edc53b4e89


### Code Distribution
* **App Basic**
  * Mingyuan Sun: Deployed default Flask framework; initialized and implemented database.
  * Asya Dente: Designed the logo; built the header.
  * Xinyang Cheng: Built the navbar and footer; defined flash messages' style and categories; modified endpoint handlers for better UI.
  * Yingru Zou: Designed the app features and functionalities; identified the target audience; linked pages logic; designed the UI/UX of login page, forget password page, and registration page.
* **Home Page**
  * Xinyang Cheng: Constructed frontend templates; applied backend page logic; added scripts to improve UI.
  * Mingyuan Sun: Applied backend logic for Tarot API and Quotes API.
* **Login Page**
  * Yingru Zou: Designed and built login page; designed a web template on Figma.
  * Xinyang Cheng: Wrote page logic to enable the login functionality.
* **Registration Page**
  * Yingru Zou: Designed and built registration page; designed a web template on Figma.
  * Xinyang Cheng: Wrote scripts to make the page more interactive; added page logic to enable the register functionality.
* **Roommates Page**
  * Asya Dente: Constructed the frontend template for the page.
  * Donovan Eyer: Wrote scripts and improved page logic to improve UI.
  * Xinyang Cheng: Added page logic to dynamically display roommates information; modified scripts and HTML.
* **Personal Profile**
  * Xinyang Cheng: Added page logic to the profile page; applied the profile-update functionality with an upgraded edit template.
  * Donovan Eyer: Constructed the profile-view template and a profile-edit template.
* **Resources Page**
  * Donovan Eyer: Finished Zillow API request logic, but the platform refused to provide information to student projects.
  * Xinyang Cheng: Finished Yotpo API request logic, but the products there were irrelevant to off-campus housing.


### Future Expectation
Currently, the login and register pages have templates that do not fit a web screen. A better design is necessary.

Registration Page: 

<img width="1205" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/19ed17bc-26d3-4ca6-9a0e-74ff446120a7">

Login Page: 

<img width="1142" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/0cf69363-3cd6-4634-8f32-a0fcf6df15ea">

Forgot Password Page: 

<img width="1192" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/9ba39e8f-61ac-44e8-a2ff-1f5f5679c3d4">

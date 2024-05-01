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
* Since `README.md` cannot handle a video that is too long, this demo does not display all implemented page logic, features and templates.
   * **unshown features:** auto logout due to session expiration; registration/update profile restriction rules; dynamic templates for profile and roommate pages; abnormal session detection; custom lines for categories storing `None`

https://github.com/TommyCheng023/CS-411-Group-Project/assets/115842289/5bf57e59-8ce7-4524-b180-a5edc53b4e89


### Code Distribution
* **App Basic**
  * **Mingyuan Sun:** Deployed default Flask framework; initialized and implemented database.
  * **Asya Dente:** Designed the project logo; built the header and the navbar.
  * **Xinyang Cheng:** Modified the navbar and footer; defined flash messages' style and categories; managed endpoint handlers.
* **Home Page**
  * **Xinyang Cheng:** Constructed frontend templates; applied backend page logic; added scripts to improve UI.
  * **Mingyuan Sun:** Found two APIs; applied backend logic and a frontend template for Tarot API and Quotes API.
* **Login Page**
  * **Yingru Zou:** Designed and built the login page; designed a web template on Figma.
  * **Xinyang Cheng:** Implemented page logic to enable the login/logout functionality.
* **Registration Page**
  * **Yingru Zou:** Designed and built the registration page; designed a web template on Figma.
  * **Xinyang Cheng:** Wrote scripts to make the page more interactive; added page logic to enable the register functionality.
* **Roommates Page**
  * **Asya Dente:** Constructed the frontend template for the page.
  * **Donovan Eyer:** Wrote scripts and improved page logic to improve UI.
  * **Xinyang Cheng:** Added page logic to dynamically display roommates information; modified scripts and HTML.
* **Personal Profile**
  * **Donovan Eyer:** Constructed a profile-view template with a profile-edit template. 
  * **Xinyang Cheng:** Added page logic to the profile page; applied the profile-update functionality with an upgraded edit template.
* **Resources Page (unused)**
  * **Donovan Eyer:** Finished Zillow API request logic, but the platform refused to provide data for student projects.
  * **Xinyang Cheng:** Finished Yotpo API request logic, but the products were irrelevant to off-campus housing.


### Future Expectation
Currently, the login and register pages have templates that do not fit a web screen. A better design is necessary.

Registration Page: 

<img width="1205" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/19ed17bc-26d3-4ca6-9a0e-74ff446120a7">

Login Page: 

<img width="1142" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/0cf69363-3cd6-4634-8f32-a0fcf6df15ea">

Forgot Password Page: 

<img width="1192" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/9ba39e8f-61ac-44e8-a2ff-1f5f5679c3d4">

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
# Current Plan
## Topic: Off-Campus Roommates Marketplace
Have no idea who to live with? 

### Humanization Roommate Matching Software For BU Community!

### Roommates Matching Main Page
* to post personal information, each user needs to provide his/her/their **age, gender, academic classification, building preference**, which will be displayed as an independent `card` on the roommates page
* each `card` has two buttons: `read more` and `contact`
  * `read more`: a pop-up window showing **the user's informative short self-description**, **the user's expectation of roommate(s)**, **monthly rent budget ($)**
  * `contact`: `<a href="mailto: ***@bu.edu"><button>contact</button></a>`, just let users contact each other directly through email, none of our business at this point :D
* filter: categorize roommates into `gender`, `age` and `building preference`

### User Registration Page
* register using **BU Email Only**, (DUO Authentication preferred), the email will be stored in the database as `contact info`
* each new user has to fill out a questionnaire with the following:

`()` means multiple choice questions, `[]` means restriction on free response questions
  1. name
  2. gender (man, woman, prefer not to talk)
  3. academic classification (freshmane, sophomore, junior, senior)
  4. age [number only]
  5. building preference
  6. monthly rent budget in dollars [number only]
  7. self-description  [150 words]
  8. roommate-expectation  [150 words]
* setup a password and reenter it
* after the registration is done, user will be sent to `roommates matching main page`
* at the same time, the user's own profile will automatically be displayed as a `card` on `roommates matching main page`

### Registration Page Future Expectation
<img width="1205" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/19ed17bc-26d3-4ca6-9a0e-74ff446120a7">


### Login Page
* enter **email and password** to login
* `Forget Password`: a small subline under the login button

### Login Page Future Expectation
<img width="1142" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/0cf69363-3cd6-4634-8f32-a0fcf6df15ea">


### Forget Password?
* verification code through email

### Forget Password Future Expectation
<img width="1192" alt="image" src="https://github.com/TommyCheng023/CS-411-Group-Project/assets/123038158/9ba39e8f-61ac-44e8-a2ff-1f5f5679c3d4">


### Remove Posting
* the user's own posted `card` has a `remove` button replaced by `contact`, once there's no need to find roommates, the `card` can be removed from the page by pressing the button
* if removed, the button will be changed into `repost` so that the user can match a new roommate in the future
     

# Pitches-app
This is a  python/flask web application where users have 60 seconds to write out their pitches in different categories and have those pitches voted on. The users also have a chance to comment on each pitch posted.
 
 ## Author
By **[IAN OTIENO](https://github.com/ian-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user.

* Logs in into the application
* Sees various categories for the pitche
* Selects the ones they prefer and see available pitches in that category
* Upvote or downvote a pitch
* Leave a comment on different pitches
* Post their own pitches
* Upload their profile photos and update thier bio

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| User signs in or creates a new account | **On page load** | user sees various categories for the pitches and the pitches posted |
| User clicks on a category | **On  click** | Various pitches of that category are displayed |
| user clicks on upvote or downvote | **Click** | values for upvote and downvote increase and decrease by one respectively |
| user clicks on comment | **On page load** | comment page is loaded where users can write and post thier comments |
| user clicks on profle  | **Click on profile** | profile page is loaded and users can can upload profle photos, update their bio and see various pitches they posted |


## Python version 
* Python3.8

## Setup/Installation Requirements
* Clone [this repository]( https://github.com/ian-otieno/pitches-app.git)  using the following commamnd  in the terminal: `git clone  https://github.com/ian-otieno/pitches-app.git`. 
* Note:<em>You will need to git installed in your machine. You can install using the following command: `$ sudo apt-get install git.`</em>
* After cloning, use command cd pithes-app.git and open using your code editor. 
* Create a vitual environment using the following command `python3 -m venv --without-pip virtual`
* Activate the virtual environment using the following command ` . virtual/bin/activate`
* Run this command  to interact with the application `$python3.8 manage.py server`
* Run tests units using the this command `$python3.8 manage.py test`

## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Flask
- Heroku

## Contacts

Email: ian.otieno@student.moringaschool.com

 &#169; 2022 Ian Otieno
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


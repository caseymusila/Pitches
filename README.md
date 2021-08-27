# Pitch

## Author

Casey Musila

## Description

This is a flask application that allows users to sign up and create one minute pitches for different categories. It also allows users to comment, upvote and downvote on pitches they have created or those created by others.

## Behavour Driven Development

- The app loads to landing page with navbar and links to see all pitches,navbar, and login button.
- Selecting the Login Button redirects to login page where the user is required to fill in a form with their Username and password. If user does not have an account they click a link to sign up. Once a user is logged in the app redirects to index page with navbar containing links to pitches,add a pitch, user's profile and logout.
- Selecting Signup redirects to the signup page and a user is required to fill in form with email,username and password. Upon submittion, page redirects to the login page for the user to signin to their account. A confirmation message is also sent to users email address thanking them for creating an account.
- Selecting Pitches redirects to pitches page with a list of all pitches in their categories. A user can upvote and downvote on all the different pitches. A user can also comment on pitches.
- Selecting the comment button will redirect to the comment page where a user can fill in a form with comments.Upon submittion their comments will be displayed at the below the form.
- Selecting the profile buttone on the navbar will redirect to the profile page where the user can be able to create a bio, upload a profile pic and also see how many pitches they have created, and the number of comments they have made.

## Installation

- Clone the repository
- cd into the cloned repository and install requirements.
- Export configurations
- Run the Appliction
- Alternatively, the project can be viewed by clicking this [link](https://pitches1965.herokuapp.com/)

## Technology Used

- Python
- Flask
- Heroku
- HTML
- Bootstrap

## Known Bugs

Boostrap is not rendering in pitches display page.

## Contact

For any comments,questions and concerns feel free to contact me via my email: musilacasey@gmail.com.

## License

Copyright &Copy: 2021 Casey Kyalo.
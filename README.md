# Felipe Spoliante Litran Portfolio - The Football Museum

![home](https://user-images.githubusercontent.com/45206652/91416594-e4636100-e84f-11ea-905c-86d78507ef97.PNG)

## About
You’re [here](https://fsl-pandorabox.herokuapp.com/) because we share the same passion for the greatest invention of mankind. If 70s, 80s, 90s and early 00s football/soccer is totally your vibe, you have come to the right place!

#### Functionalities
The app was built with the use of the Django framework. Django makes it simple to split the different functionalities of the website by treating each one of them as a separate application, and managing its core by the admin panel.
The development of The Football Museum was entirely done with the use of GitPod, while its version control sytem was done with the use of GitHub.

The application consists of 6 main sections providing the user with the possibility of:
1. Homepage: Find their favorite football shirts of their favorite clubs and heros
2. All Shirts: This section contains all available products of The Football Museum
3. Search: A search bar in order to facilitate for the user to locate his or her favorite products
4. My Account: The account preferences/details make possible for users to insert their personal preferences so we at The Football Museum can have new products available for them
5. Cart: The shopping cart is where the user can see a summary of the itens selected by him/her
6. Contact: The contact section is where our users can directly communicate to us a product which is currently not available

#### Goal

The application is designed for football fans who are passionate about historical football shirts from the most iconic squads in football history.

## UX

#### Layout
 
- The Multiple Page Apps (MPA) design and CRUD charactheristic of the app make possible for the users to insert their account details and personal preferences as a football in order for us at The Football Museum to have the best available product line.
- The database selected was Postgres, hosted by Heroku. All static and media files are hosted by Amazon S3 services.
- The app is designed by applying a user-friendly concept making it easy for users to find their favorite football shirt.

#### Colour Scheme

- Taking into account the main theme of the app, the idea is to associate the colors to a football pitch.
- [Adobe Color](https://color.adobe.com/create/color-wheel/) provided me with complementary, compound, analogous, and monochromatic shades of grey and white.
- Color
    - ![#28A745](https://placehold.it/15/28A745/000000?text=+) `#28A745` color description: Green
    - ![#fff](https://placehold.it/15/fff/000000?text=+) `#fff` color description: White
    - ![#212529](https://placehold.it/15/212529/000000?text=+) `#212529` color description: Grey

## Technologies Used

#### Languages Frameworks Tools

- HTML5
- CSS3
- Django
- Python3
- Gitpod
- Github
- Postgres
- Amazon S3
- Bootstrap 4.4
- Heroku
- jQuery 3.2.1
- Font Awesome - v4.7.0

#### Other Resources

- [Adobe Color](https://color.adobe.com/create/color-wheel/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

## Features

#### Existing Features

As the applications consists of a MPA, I applied an easy navigation where the user can clearly see where to search, login, register, checkout or edit his or her account:

- Checkout - Shipping Address: If the user has already registerd and completed his Account Details section, hist or her shipping address, when checking out, will be the same one present in the user's profile. 
- Fan Information: In the Fan Information section the user has the possibility to add his or her favorite club, hero, shirts and size.

#### Features Left to Implement

- I want to update the website name as it is currently displaying the former name give to the app.
- I wish to implement a section where users can have their credit card and billing information saved, which can then be used for future orders.
- A new product line where football boots from the 70 and 80s can be purchased by the fans.

## Syntax Testing

Resources & Tools Used for Testing

#### HTML
-[W3 HTML Validator](https://validator.w3.org/)

#### CSS
-[W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Responsiveness

- Responsive design has been applied to all kinds of devices including phones, tablets, laptops, and desktop views. 

#### Testing

[![Build Status](https://travis-ci.org/Litran1990/DjangoMilestoneProject.svg?branch=master)](https://travis-ci.org/Litran1990/DjangoMilestoneProject)

- a) In this session, a new user has been registered usign the criteria set shown below:
    1. Email address: testing2@testing2.com
    2. Username: testing2

- b) Here the idea was to logout and login with the newly introduced user 'testing2':
    1. Username: testing2

- c) In this session, the goal was to add multiple products to the shopping cart. One product from the 'Recently Added' section and the second one from the 'All Shirts' page:
    1. Home Page - Recently Added: '1999-00 Man United Home - M'
    2. All Shirts: '1996-97 Palmeiras Home - L'

- d) The fourth test was done by completing the user Account Details

- e) The fifth test was done to check the payment funtionality by performing a checkout, where the Shipping Address should be already filled out as the user has completed his Account Details page:
    1. Credit card number: 42424242 42424242 (Strip Test Data)
    2. Security code (CVV): 123
    3. Month: 1
    4. Year: 2021

- f) The final test was done by sending a message to The Football Museum by using the Contact funtionality:
    1. Email: testing2@testing2.com
    2. Reason: Test
    3. Message: Testing message.

#### Testing Outcome

- a) As expected the user was successfully registered:

![registered](https://user-images.githubusercontent.com/45206652/91453009-8babbc80-e87f-11ea-8290-11e3dcd2d1e0.PNG)

- b) As expected the user was able to logout and successfully login:

![login](https://user-images.githubusercontent.com/45206652/91453584-3a4ffd00-e880-11ea-9ddd-cb658590021e.PNG)

- c) The two products from two different pages were successfully added to the shopping cart:

![cart](https://user-images.githubusercontent.com/45206652/91454197-f90c1d00-e880-11ea-9649-f453e69aee02.PNG)

- d) The test passed and the user was able to edit his Account Details webpage:

![account1](https://user-images.githubusercontent.com/45206652/91454532-5c964a80-e881-11ea-9e5a-67d83f79bde1.PNG)

![account2](https://user-images.githubusercontent.com/45206652/91454893-bdbe1e00-e881-11ea-8b34-086b615afb25.PNG)

- e) The payment was successfully submitted and the Shipping Address form was correctly showing the user info inserted in the Account Details page:

![checkout1](https://user-images.githubusercontent.com/45206652/91455373-48068200-e882-11ea-8ef8-0e364d99ad58.PNG)

![paid](https://user-images.githubusercontent.com/45206652/91455673-aaf81900-e882-11ea-9d88-7de7ec89c60e.PNG)

- f) The contact form was successfully sent to The Football Museum:

![contact](https://user-images.githubusercontent.com/45206652/91456178-41c4d580-e883-11ea-8c51-6fef485258ef.PNG)

![contact2](https://user-images.githubusercontent.com/45206652/91456275-5acd8680-e883-11ea-80fc-31e456e88674.PNG)

#### Issues During Testing Sessions & Design

- I had a few bugs and erros when adding new fields, changing forms or excluding fields/forms in the existings models which already contained live data (seen in the admin panel).
The solution for such error was to delete the existing database in order to be able to migrate the updates and successfully manage the admin panel:

- Here below there is a really useful tutorial when encountering migration erros such as the one described above:

![reset-migrations](https://user-images.githubusercontent.com/45206652/91458585-fbbd4100-e885-11ea-936e-ac1167670f21.PNG)

- Also, as I'm currently hosting all static and medial fils with the use of Amazon S3 services. Therefore, once these files have been updated, they must be sent from the local repository to AWS S3 by running the following CLI command: ['python3 manage.py collectstatic'](https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/).

## Deployment

This website is hosted on Heroku, and it is deployed automatically from its master branch on GitHub. Therefore, once a new commit has been done the changes will automatically take effect on the live application. 

Additionally, if you wish to run the code locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/Litran1990/DjangoMilestoneProject` into your terminal. In order to cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

## Credits

#### Media
- The photos used in this project were obtained from [Bing Images](https://www.bing.com/).

#### Acknowledgements

- I received inspiration for this project from:
 1. Code Institute's Data Centric Module - Mini Project
 2. [Classic Football Shirts](https://www.classicfootballshirts.co.uk/)
 3. [Vintage Shirts](https://www.vintagefootballshirts.com/)
 4. [RB Jerseys](https://www.rb-jerseys.com/)
 4. [Django Tutorials by Max Goodridge](https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj)
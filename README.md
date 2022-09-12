# Football Casuals

![](static/homepage.jpg)

[View deployed site here](https://footballcasuals.herokuapp.com/)

Football Casuals is a online clothing store specialising in the 'Casuals' genre.
Selling specialist range clothing from brands such as fila, ellesse, sergio tachini and many more. Customers can register for an account which gives them access to the blog, this also allows them to add products into their bag to purchase. All users can browse the products however they wont be able to add into the bag until they log in. Admin / Staff users can delete products if they are no longer available, they can also add new products onto the site that have came into stock. All users can then also go into the contact section to which they are presented with a form so that they can ask any queries or for if they are after a certain product sourcing that isnt currently on the site.

The site is laid out with clear information, minimalistic design so that the user can take in all the information in front of them. All products are laid out neatly with the product image taking centre stage to really try and sell the products themselves. The checkout process is simple and effective allowing for ease of purchase with then a confirmation email sent to the user to confirm that their order has reached the shop and will be despatched as soon as possible.

## Planning

- [View website planning Q's](https://docs.google.com/document/d/1C3_8yjV5OL-vI_vUVK-uQ40GAQa17Ybtdwm-NSfwbU4/edit?usp=sharing)
- [View homepage design](static/home_page.png)

- The main theme of the website was constructed through the original mockup which then allowed me to create the base.html. From here i used the user stories and feature planning to really design
the page and this allowed me freedom with the project creation scope to get creative and take time to see what worked best and where.

## User Stories

1. As an admin user I want to be able to add new products onto the site
2. As an admin user I want to be able to delete products once they are no longer available
3. As an admin user I want to be able to delete blog posts
4. As a site user I want to be able to see what the site is going to offer me
5. As a site user I want to be able to browse the products that are on sale
6. As a site user I want to be able to choose with size I want for a particular product
7. As a site user I want to be able to choose the quantity of a certain product that i am buying
8. As a site user I want to be able to get in touch with the store online
9. As a site user I want to be able to chat to fellow fashion lovers like myself
10. As a site user I want to be able to get my own account
11. As a site user I want to be able to pay via the website online

## Features

### Base Template

- The head of each page includes the nav bar primarily which consists of the brand logo and the navigation links. The logo is a link to the home page that can be used from any webpage
within the website
- Non-logged in users see products, account register and login, blog (although cannot access the page, automatically directed to login page)
and contact links
- Logged in users see products, blog, contact, and logout
- Admin users see all of the above plus a manage tab which is used for staff members to easily add products through the front end

### Home page

- Home page starts with a related image of a football stadium, due to the casual fashion sense having links to the football culture
- Page is then split up into 3 major website categories, one being the card explaining information about the business,
the other being a short description of products on offer with a button link to the products and the last one introducing the blog part
of the site and a note around expectation of user behaviour.
- The newsletter powered by mailchimp is also here to allow users to subscribe for latest information and offers

### Products page

- All products are listed on this page, in a responsive manner, which consist of a card for each product with the related information i.e name, description
pricing and category. All products are links to which logged-in users can see the product detail page.

### Product Detail page

- Admin users have access to a delete function of this page which allows them to delete a product from the database, for situations where the item may now be
out of stock of discontinued
- This is where the logged in user can choose the product size and the quantity of products that they would like to purchase, they then do this by clicking the add to bag button.
Users also have a button for keep shopping which will return them to the products page to add more products into their bag

### Product Delete page

- This is a simple display page that emphasises the importance to confirm this is the action the admin wants to take as this can cannot be undone.

### View bag page

- This page is only accessable for logged in users, this gives them a table to display their product that they have put into their basket with all the relevant information, for
example the size that they picked and the quantity.
- The bag total is also displayed so that the user can see how much the order is going to cost them if they do wish to checkout
- Users are able to click 'remove' in which they can remove items from their basket that they do not need, if they remove all products from their bag, the whole display of the page
changes to show no products are in the bag and a sad-face icon.

### Checkout page

- This page again shows the users basket to double check that everything is still correct and the user knows exactly what product they are ordering and how much the outstanding balance
is for them to pay.
- On the right hand side of the page, there is then a form for the user to input their details for delivery and payment
- At the bottom of this section their is then the stripe payment box to add the card details in for the user, this validates while inputting to ensure that the card details are correct before continuing with the order.

### Order-Confirmation page

- This page quotes the order number that was just created for the user, shows them again the items and the amount they have paid. There are also messages that confirm the same thing if the purchase has gone through.

### Blog page

- This page shows the blog post topics that are currently open with their title and description with a handy button to enter into the blog chat.

### Blog Comment page

- This page shows the topic details to the top of the page
- A convenient body field to input their message and a button below to post
- Below this there is then what resembles a chat layout, which quotes the date and time posted, the users name and finally their message
- On messages that have been created by that particular user (or admin) there is also a delete function to remove comments from the blog discussion

### Contact page

- This page is accessible by all users and opens a form with fields for name, email and message and a submit button
- Open a form submit the page will then reload to allow for any other requests

### Manage page

- This page is for admins only as this is the form that allows users to add a new product onto to the system, with all the relevant fields to match up to the back-end data model
- Upon completion of this form there is then a redirect onto the products page where the new product will display alongside the others, as well as a temporary message at the top of the page.

### Continous Improvement Features

- I would like to create a proper functioning profile app
- I would like to develop the admin front end features further so everything is accessibile
- Add full CRUD functionality to all website features for appropriate users
- Create a stock system instead of admins currently needing to delete products

## Technologies Used

- HTML5
- CSS
- Python
- Postgres
- Cloudinary
- Bootstrap
- Font Awesome
- Google Fonts
- Django
- Stripe
- Django Allauth
- Gunicorn
- DevTools
- Visual Studio Code
- Heroku

## Business Model / Marketing

### Business Model

Football Casuals is B2C(Business to customer) application due to the fact that it is primarily intended and designed around a individual client creating single orders. They can purchase clothing items online via a single payment and they will be delivered to their location of choice.

### Marketing

- Social media is arguably the best source of marketing for the modern world, this store has also got a facebook account to put itself on the market and advertise its purpose further
- Meta tags used within the website to improve the SEO
- Email newsletters via the Mailchimp utility
- [View facebook page](static/facebook_page.png)

## Agile Methodology

- [View Google Docs Agile Job Board](https://docs.google.com/spreadsheets/d/1QLs2885t0_M3ZYBUZVLHK893Sn1aK-klLWDD3ABH0Us/edit?usp=sharing)
- Github project board also set to Public

## Testing

### Automatic Testing

- W3C HTML Testing Service - Ok
- W3C CSS Testing Service - Ok
- PEP8 Testing Service - Ok
- JSHint Testing Service - Ok

### Manual Testing

- DevTools - Dev tools was used through the project to test responsiveness, and design layouts
- Stripe false bank cards - To put purchases into practise to carry out testing and handle checkout correctly.

## Deployment

### My project deployment

- This project is deployed via Heroku
- My project was created in Gitpod
- Git was used for Version Control
- My project was deployed once I had completed the majority of manual testing.

### Deploying Via Heroku

Create an env.py file, you will need the following variables for your project at a minimum -

- SECRET_KEY: (randomly generated)
- CLOUDINARY_URL: Copy your CLOUDINARY_URL from the dashboard
- DATABASE_URL: This is the value of DATABASE_URL in Heroku
- Make sure in settings.py to set the ALLOWED_HOSTS value to use your localhost and Heroku app name.

### Deploying to Heroku

To deploy to Heroku follow these steps:

1. Locate the New button at the top right end side of the dashboard.
2. Click on Create new app, select your region and pick a suitable name for your project.
3. In Settings add buildpack Python.
4. Add Database to App Resources. Go into the Resources Tab then Add-ons then search and add Heroku Postgres.
5. In the Settings Tab, in Config Vars, make sure you have the DATABASE_URL added with the previous step and to add the other variables: SECRET_KEY and CLOUDINARY_URL. Ensure the variables here are then matched up with the env.py
6. Select Deploy from the navigation bar
7. Select the deployment method of Github and seach for your repository.
8. Proceed to link the Heroku app to the repository by clicking on connect.
9. Click on Deploy.

### Forking a Repository

- Forking is a good utility to use to make a copy of an original repository so that this can be edited without making any changes to the original development repository.

- Locate a repository you wish to copy

- The Fork button is above the repository control bar to the right.

- Once clicked this will then create the repository copy to your Github account.

### Cloning a Repository

- You can clone a repository straight to Gitpod if needed.

- Locate a repository you wish to clone

- Just below the repository control bar, there is a green Gitpod button.

- This will then open the project in Gitpod for you (if gitpod is installed).

## Credits

- Reuben Ferrante - CI Mentor
- 80s Casuals Classics LTD - Product Images
- Google images - I do not own copyright to any images used within the site
- Slack - Student Chat Platform
- Stack Overflow - Coding Aid

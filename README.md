# Football Casuals

![](static/homepage.jpg)

[View deployed site here](https://footballcasuals.herokuapp.com/)

Football Casuals is a online clothing store specialising in the 'Casuals' genre.
Selling specialist range clothing from brands such as fila, ellesse, sergio tachini and many more. Customers can register for an account which gives them access to the blog, this also allows them to add products into their bag to purchase. All users can browse the products however they wont be able to add into the bag until they log in. Admin / Staff users can delete products if they are no longer available, they can also add new products onto the site that have came into stock. All users can then also go into the contact section to which they are presented with a form so that they can ask any queries or for if they are after a certain product sourcing that isnt currently on the site.

The site is laid out with clear information, minimalistic design so that the user can take in all the information in front of them. All products are laid out neatly with the product image taking centre stage to really try and sell the products themselves. The checkout process is simple and effective allowing for ease of purchase with then a confirmation email sent to the user to confirm that their order has reached the shop and will be despatched as soon as possible.

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

## Business Model

Football Casuals is B2C(Business to customer) application due to the fact that it is primarily intended and designed around a individual client creating single orders. They can purchase clothing items online via a single payment and they will be delivered to their location of choice.

## Agile Methodology

[View Google Docs Agile Job Board](https://docs.google.com/spreadsheets/d/1QLs2885t0_M3ZYBUZVLHK893Sn1aK-klLWDD3ABH0Us/edit?usp=sharing)
- Github project board also set to Public

## Deployment
## My project deployment

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
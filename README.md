# [The Cocktail Companion]

![The Cocktail Companion Responsive](/thecocktailcompanion/static/uploads/cocktailCompanionResponsive.png)

## Live Link [https://cocktailcompanion.onrender.com/](url)

## Contents

1.

# <a name="summary"></a> Summary

This site is a helper for all mixologists out there designing and creating their own drinks.

It provides a database of classic cocktails with images and specs. Upon signing up and loging in it allows the users to create, read, update and delete their own cocktails.

# <a name="UX"></a> UX

## <a name="Strategy"></a> Strategy

### **New site user's goals:**

- As a new site user, I want to be able to browse Classic Cocktail recipe's.
- As a new site user, I want to be guided to where to log in and create my own account.
- As a new site user, I want to have a clear understanding of how the site works through good UI/UX design.
- As a new site user, I want to easily navigate throughout the site.

### **Returning site user's goals:**

- As a returning site user, I want to be able to Log in to my account.
- As a returning site user, I want to be able to upload my own recipes.
- As a returning site user, I want to be able to edit and delete those recipes.
- As a returning site user, I want to be able to view my uploaded drinks without seeing the recipe so I can revise the specs within the app.

### **Site owners goals:**

- As the site owner, I want the pre supplied recipes shown to everyone but for users to only have access to their own recipes.
- As the site owner, I want an admin account where I can periodically add new cocktails for everyone to see.
- As the site owner, I want the site fully responsive as mixologists and bartenders only have access to their phones behind a bar.

## <a name="Scope"></a> Scope

**Functional Requirements:**

#### For ease of use:

- Navigation bar which is simple and easy to use.

#### To ensure database CRUD functionality

- Function to add recipe
- Function to edit recipe
- Function to delete recipe
- For each recipe to only be viewed and editable by the owner.

**Visual requirements**

#### To ensure the users eyes are drawn to specific content:

- Images and names of cocktails
- Where to sign up/log in

#### For usability

- Cocktail specs to be hidden behind a button so users can use the site as flash cards to revise their cocktials.

## <a name="Structure"></a> Structure

**Interactive design**

- User friendly design and visually appealing interface to make users feel cofortable and likely to return to the site.
- Responsive layout for use on either desktop or mobile.

**Information Architecture:**

- Nav bar at the top of the page
- Footer locked to the bottom of the page.
- Responsive nav bar that hides behind a burger icon on mobile.
- Responsive and auto sized images upon upload.
- All information is appropriate and relevant to the subject and is not misleading or hard to find.

## <a name="Skeleton"></a> Skeleton

![The Cocktail Companion Wireframe](/thecocktailcompanion/static/uploads/TheCCWireframe.png)

## <a name="Surface"></a> Suface

The intention of the web app is to be as user friendly as possible whilst having a branded look and feel to it.

# <a name="Features"></a> Features

## <a name="Existing Features"></a> Existing Features

| Feature         | Details                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Sign Up         | The user can sign up to be able to add and edit thier own cocktail recipe's                                                   |
| Log In          | The user can log in to their account to see their prior uploaded cocktails and edit them as they wish.                        |
| Add cocktail    | This feature allows users to be directed to a form set up to build the card for their new cocktail                            |
| Upload image    | Allows users to upload the image they would like above the title on their cocktails card in the library                       |
| Edit cocktail   | This redirects the user to an edit form allowing them to adjust any recipe details they wish                                  |
| Delete cocktail | This gives the user a pop up/ flash to check they want to delete the cocktail and remind them that this is a permanent action |

## <a name="left-to"></a> Future implementations

| Feature         | Details                                                           |
| --------------- | ----------------------------------------------------------------- |
| Search feature  | Allow users to search for coktails by recipe name                 |
| Filter function | Allow users to filter their cocktails by ingredients or certain o |

ther parameters
Stock feature | Allow users to add a list of what ingredients they have to hand to see what cocktails they can build now and what is missing to make similar ones

# <a name="tech"></a> Technologies used

- Materialize - https://materializecss.com/
- JavaScript
- Google fonts - https://fonts.google.com/
- www.validator.w3.org
- http://www.css-validator.org/
- Git
- GitHub
- Google Chrome
- Mozilla Firefox
- http://www.responsinator.com/
- Chrome Dev Tools
- Firefox Dev Tools
- Python
- Flask
- PostgreSQl
- Heroku
- Jinja
- Favicon.io
- Figma

# <a name="testing"></a> Testing

### **New user site testing:**

- As a new site user, I want to be able to browse Classic Cocktail recipe's.

* Upon entering the Library section all the sitea 'Classic Cocktails' are there to be viewed.

- As a new site user, I want to be guided to where to log in and create my own account.

* In the nav bar and footer are clear buttons to direct the user to sign up to be able to make their own drinks.

- As a new site user, I want to have a clear understanding of how the site works through good UI/UX design.

* This is evident throughout the site.

- As a new site user, I want to easily navigate throughout the site.

* This is achieved through the responsive nav bar on all screen sizes.

### **Returning user site testing**

- As a returning site user, I want to be able to Log in to my account.

* This is achieved through the log in button on the nav bar.

- As a returning site user, I want to be able to upload my own recipes.

* Once logged in the user is able to upload their own recipes.

- As a returning site user, I want to be able to edit and delete those recipes.

* Once logged in the user is able to edit and delete their recipes.

- As a returning site user, I want to be able to view my uploaded drinks without seeing the recipe so I can revise the specs within the app.

* This is achieved through the card system so only the name and picture are visible until clicked on to allow easy revision.

### **Performance testing:**

1. Tested website responsiveness using http://www.responsinator.com/
   1. Results: The website is responsive to all device sizes without any unnecessary x-scroll.
1. Tested the image size to ensure no image is to large and impacting the website loading times. I used the Google Dev Tools - Network
   1. Results: The site loading time is sub optimal. The total website loading time is 1.35s which can be improved
1. Tested the images on all pages using Google Dev Tools - Lighthouse
   1. Results: An issue highlighted using this tool is the image formats used. Image formats like JPEG 2000, JPEG XR, and WebP often provide better compression than PNG or JPEG, which means faster downloads and less data consumption.
1. All HTML pages were tested using https://jigsaw.w3.org/css-validator/validator
   1. All pages passed without any errors.
1. Tested the CSS using http://www.css-validator.org/
   1. The only errors found were within the Materialize minify settings so no errors with the actual code of the site.
1. Tested the website on the Google Chrome browser Version 87.0.4280.88 (Official Build) (64-bit)
   1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Microsoft Edge browser Version Version 87.0.664.66 (Official build) (64-bit)
   1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Firefox browser Version 82.0.3 (64-bit)
   1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the form validation worked correctly on each of the above browsers
   1. Results: The form correctly sent when the fields were completed as they should have been and did not when the fields had not been completed

# <a name="deployment"></a> Deployment

## <a name="github"></a> Github Pages

1. Create a new repository or access an existing repository
1. Click the green Gitpod button to launch the project in Gitpod
1. Create an index.html file
1. Add the file to the staging area using the git add Functional
1. Commit the file using the git commit function, adding an appropriate commentary
1. Push the file to GitHub using the git commit and git push functions
1. Refresh your GitHub repository and click the 'Settings' tab
1. Scroll to the GitHub Pages section and select a publishing source
1. Click 'Save'
1. Click the URL created within the Settings - GitHub Pages section

**To clone the repository for local deployment:**

1. On the main page of the repository, click the down arrow Code button
1. Click the download icon under the relevant section to clone with either HTTPS, SSH or GitHub CLI
1. In Git Bash, change the current directory to the location you want the directory to be stored
1. Type git clone and then paste the URL you copied in step 2
   1. An example for HTTPS: `git clone https://github.com/hollyford/recipe-nation`
1. Press enter - that's it, your clone has been completed!

**To fork the repository:**

1. Navigate to the main page of the repository you wish to fork
1. Click the Fork button on the top right hand side of the page

## <a name="heroku"></a> Heroku

### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/hollyford/recipe-nation), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('recipe-nation') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the env.py file created earlier:

| **Key**              | **Value**                                                                                        |
| :------------------- | :----------------------------------------------------------------------------------------------- |
| IP                   | `0.0.0.0`                                                                                        |
| PORT                 | `5000`                                                                                           |
| SECRET_KEY           | `<app secret key>`                                                                               |
| MONGO_URI            | mongodb+srv://root:r00tUser@cluster0.4zi37.mongodb.net/recipe_nation?retryWrites=true&w=majority |
| MONGO_DBNAME         | `recipe_nation`                                                                                  |
| S3_BUCKET            | `recipe-image-repo`                                                                              |
| S3_ACCESS_KEY        | `<S3 key>`                                                                                       |
| S3_SECRET_ACCESS_KEY | `<S3 secret key>`                                                                                |

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard.

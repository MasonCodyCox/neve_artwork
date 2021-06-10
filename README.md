# Neves Artwork

Weclome to my artwork website based on Neve's artwork. this website should be able to advertise her work 
in a way that users wil be drawn in to purchase it.

I want users to be able to log in and view items based on a sett of filters they choose. This will be very good for user experience 
as this will narrow down searches to whatt users are most interested in.

## Design Process 

When i initally thought about creating this artwork store, I sketched some ideas down onto my IPad. 
Learning to what extent you can customise your site with the power of django and allauth, there are endless ideas 
that i would love to impliment throughout my site. Having the power of a super user really changed my perspective on the site too. 
A super user enabled the site creator/ any admins to have full CRUD functionality within the site.

## Wireframes/ Mock ups

- These are all found within the assets folder. Please go to assets > wireframes.

## User Experience

### User Stories

* I want to be able to store information for log in.
* I want to be able to search for a specific piece of artwork.
* I want to be able to update my information or delete it if needed.
* I dont want other people to be able to update or delete my information.
* I want an easy navigation layout for the website.

These needs are met by;

* Implimenting allauth within my website.
* A navbar search bar for the entire site. (work in progress)
* A profile page for users to access. (work in progress)
* A simple yet effective navigation bar that will not break from clicking between pages in any 
order. And, adapts to screen size.

### Strategy Plane 

##### Website Goals;

* A safe way to store information.
* Create an easy to use website.
* Use simple yet effective ways to impliment allauth for ease of access.
* Create a website that would be effective in all age groups.
* Easy CRUD functionality.

### Scope Plane 

The home page contains a clear and vibrant piece of artwork designed by Neve to 
instantly display what she is capable of. The website uses a django allauth to 
store user authentication. overall, the entire site enables CRUD functionality.
The Navbar is has bootstrap implemented for ease of access from different screen sizes.


### Structure Plane 

The aim of the structure is to allow users to navigate through the site with ease. 
The home page contains a picture to instantly show users artwork.

### Skeleton Plane 

1. Navbar that changes based on device being used.
2. A dropdown navagtion icon for smaller screens.

### Surface Plane

When creating this project, I thought intensly about colours that would be good for user experience.
The colours for the main site are subtle coulours that go well together along with a bold primary colour. The 
navbar colours were a subtle grey which is easy on the eyes for every user. I want the user to feel as if they 
feel welcomed to the site.

## Features

dropdown icon - Easy navagtion for smaller devices where all pages may not fit onto the screen.

Call to action buttons - easy navigation for user from and to any page on the website.

A superuser -  easy admin CRUD functionality to the site

A sale banner - a flash message which informs the user of completion, error encounters when submitting a form.

### Features left to implement

* links to socials - easy to use icons at the bottom of every page for additional navagation/ support.

* Support page - a page in which the user can receive help/ report upon a form completion.

* I still have a lot to create in terms of building this website further. Full CRUD functionality for users within their 
profile pages would be great.

## Technologies used

[Stack Overflow](https://stackoverflow.com/) - I used this as a resource of skils that I needed to learn e.g Python.

[W3Schools](https://www.w3schools.com/default.asp) - I used this as a resource for skills e.g Styling pieces of text.

[W3Docs](https://www.w3docs.com/) - I used this to learn how to style buttons and spans.

[Geeks for geeks](https://www.geeksforgeeks.org/) - I used this to learn different attributes for HTML.

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - This was used to create my user athentication.

## Testing

-  The CSS was run through the https://jigsaw.w3.org/css-validator/ without any errors found.
-  The HTML was run through the https://validator.w3.org/, the errors that are found are all related to the Jinja 
templating.
-  The cornflakes(flake8) lint was installed as an extension to the development and validated the Python code 
throughout my milestone project.
-  The site was tested on three different browsers: Google Chrome, Brave and Safari.
-  The responsiveness was tested on a wide variety of devices such as iphones, tablets and desktops using the Chrome 
DevTools and http://whatismyscreenresolution.net/multi-screen-test.


## Issues 

- The manage documents cards didnt sit properly when a large description was added
- I had issues trying to get my started experiencing placeholder text to dissapear

### Validation

The W3C Markup Validator and the W3C CSS Validator were both used to validate every page of this project.
Despite my efforts, the vaildation had issues reading Python code. all HTML5 and CSS passed.


### Device testing

During my project, I consistently checked the website compatibility with all device sizes to ensure the best user experience possible.
I ensured this by using Chromes built in developer tools.
This website works well on all device sizes although I did encounter some issues on mobile device size with the text overflow. 
This happens when you go the the create a document page on mobiles and placeholders do not sit on their inputs.

I had a number of work collegues, family and friends try the website out for feedback so that i could make improvments from early development stages 
regarding a users experience. 


#### Devices tested

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- IPhone 5/SE
- IPhone 6/7/8
- IPhone 6/7/8Plus
- IPhone X
- IPad
- IPad Pro
- Surface Duo
- Galaxy Fold

## Credits

#### Content -

The Navbar have all been copied from Bootstrap. I have now styled it in my own way to fit into my website.
The create document form has been copied from one of my previous peices of work but styled to fit correctly with this website 
along with added Python for functonality.

[Stack Overflow](https://stackoverflow.com/) - I used this as a resource of skils that I needed to learn e.g Python.

[W3Schools](https://www.w3schools.com/default.asp) - I used this as a resource for skills e.g Styling pieces of text.

[W3Docs](https://www.w3docs.com/) - I used this to learn how to style buttons and spans.

[Geeks for geeks](https://www.geeksforgeeks.org/) - I used this to learn different attributes for HTML.

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - This was used to create my user athentication.

#### Acknowledgments

I have taken inspiration from my previous projects that have helped me construct this one. They are on my github repository
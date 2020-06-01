# InstaPic

This is python Web app made with the Django that is supposed to be a clone of Instagram. I've tweaked the UI a little bit but the basic functionality of instagram is maintained

### User Stories:
1. Sign in to the application to start using.
1. Upload my pictures to the application.
1. Search for different users using their usernames
1. See my profile with all my pictures.
1. Follow other users and see their pictures on my timeline.
1. Like a picture and leave a comment on it.

### User Journey
1. The user first registers for first time users, this will lead them to a create profile page where they can upload an image and write a bio
1. On login the user will be directed to their home/timeline where they can see the photos of people they follow,and their uploaded pictures
1. A user can upload pictures from your profile
1. A user can follow users once they search for them from the results page, they can also view the user's profile
1. On the explore page, user can see all the photos from all the users
1. a user is able to update their profile bio and/or image


## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==3.0.6

#postgres
$ pip install psycopg2 
```
### Requirements
1. asgiref==3.2.7
1. astroid==2.4.1
1. beautifulsoup4==4.9.1
1. Django==3.0.6
1. django-bootstrap4==1.1.1
1. isort==4.3.21
1. lazy-object-proxy==1.4.3
1. mccabe==0.6.1
1. Pillow==7.1.2
1. psycopg2==2.8.5
1. pylint==2.5.2
1. pyperclip==1.8.0
1. python-decouple==3.3
1. pytz==2020.1
1. six==1.15.0
1. soupsieve==2.0.1
1. sqlparse==0.3.1
1. toml==0.10.1
1. typed-ast==1.4.1
1. wrapt==1.12.1
 1. use the requirements.txt to get full list of dependencies
### .ENV file
1. SECRET_KEY='<SECRET_KEY>'
1. DEBUG=True #set to false in production
1. DB_NAME='databasename'
1. DB_USER='username'
1. DB_PASSWORD='password'
1. DB_HOST='127.0.0.1'
1. MODE='dev' #set to 'prod' in production
1. ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
1. DISABLE_COLLECTSTATIC=1

### Installation
1. To access this application on your command line, you need to clone it 
`https://github.com/martyminion/Instapic.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations photos`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test photos`


### Break down into end to end tests
### Example
  ```
   def test_get_image_by_user(self):
    images = Image.get_images_by_user(self.drew.id)
    self.assertTrue(len(images)>0)
  ```
* The above test tests if the method returns an image on lookup using the user id 

## Bugs
  No  bugs as of yet, if encountered you can get me on *martyminion0@gmail* or log an issue from github

## Future Improvements
  Have a proper explore page, and have the posibility to upload videos too
  Enable user stories

## Deployment

The app can be found live on heroku: https://lifeinpicture.herokuapp.com/


## Built With

* Python 3.6.9 
* Django Framework 3.0
* JavaScript and JQuery
* HTML and CSS

## Authors

* **Martin Kimani** 

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }


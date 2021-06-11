# MiniFlix

MiniFlix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries and more – on thousands of internet-connected devices.

You can watch as much as you want, whenever you want, without a single ad – all for one low monthly price. There's always something new to discover, and new TV shows and movies are added every week! 

(Rather a Netflix clone!)

### Instructions to run the project

1. Clone the repository.
2. cd into the project folder
3. Delete the migrations

```bash
$ python manage.py makemigrations netflixapp
$ python manage.py migrate
$ python manage.py sqlmigrate netflixapp 0001
```
You can create a superuser using the following command

```bash
$ python manage.py createsuperuser
```

5. Run the program

```bash
$ python manage.py runserver
```

## News site

To start the installation, clone the repository, then go to the directory
```cd news_medium```

Next, install the required packages:

```
python3 -m pip install -r req.txt
```

Create new migrations

```
python3 manage.py makemigrations
```

Now apply the migrations

```
python3 manage.py migrate
```

Create yourself an administrator to use the admin panel

```
python3 manage.py createsuperuser
```

Before starting the server, I recommend running the tests, as changes are possible:
```
python3 manage.py test
```

And we start the server locally with the command:

```
python3 manage.py runserver
```

## [Welcome to home page](http://127.0.0.1:8000/)

http://127.0.0.1:8000/

![This is an image main page](https://i.imgur.com/FAYNFti.png)

Without registration, the user has the opportunity to read news, view tags and search for them, as well as register and
log in.
After registering, the user immediately gets the opportunity to add his articles, as well as new tags.

Pretty good project, but in my opinion the comment system is poorly implemented. I will try to make my next project with
a more convenient comment function
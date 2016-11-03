# auth-flask-angular

copy code from:

https://realpython.com/blog/python/handling-user-authentication-with-angular-and-flask/
https://github.com/realpython/flask-angular-auth/tree/99657a8172c92f73c7fa57435b940500253dabc4

-Add:

pip install Flask-Migrate
pip install Flask-Bcrypt

-Create Initial migration:

$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate

-Install sqlitebrowser:
 
 http://sqlitebrowser.org/

from mac:

$brew cask install sqlitebrowser
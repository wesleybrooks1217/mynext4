# mynext4

## Local Environment Setup

### Virtual environment creation
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirement.txt
```

### Local database creation
Follow installation instructions [here](https://www.postgresql.org/download/). Example on macOS (with Homebrew already installed):
```
$ brew install postgresql
```

Start up psql server. Example on macOS:
```
$ pg_ctl -D /usr/local/var/postgres start
```
This will start up the database server hosted locally on port 5432.

Create a new database:
```
$ psql postgres
postgres=# CREATE DATABASE mynext4;
postgres=# CREATE USER db_admin WITH PASSWORD 'supers3cretpassw0rd';
postgres=# GRANT ALL PRIVILEGES ON DATABASE mynext4 TO db_admin;
postgres=# ALTER USER db_admin CREATEDB;
postgres=# \q
```
NOTE: example password provided, you should change this password to something else and copy it to the `'PASSWORD'` field in the the `DATABASES` dict in `mynext4/backend/backend/settings.py`.

Migrate database:
```
(env) $ python manage.py migrate
```

## Create an admin for the server
```
(env) $ python manage.py createsuperuser
```
Enter username, email, and password. Remember these credentials. You can use these to log into the admin console found at http://localhost:8000/admin/ (after starting up the server, see command below).

## Populate the data for initial testing
With the server running (see command below), navigate to http://localhost:8000/admin/college/college/ and press "Add College". Fill in all fields to start adding them to the database. Ideally, add 2-4 colleges. Here is some data you can add:
| Name | City | Public | Year est | Description |
| :-- | :-- | :-- | :-- | :-- |
| Brown University | Providence, RI | No | 1764 | Brown University is a private Ivy League research university in Providence, Rhode Island. Founded in 1764 as the College in the English Colony of Rhode Island and Providence Plantations, Brown is the seventh-oldest institution of higher education in the United States and one of the nine colonial colleges chartered before the American Revolution. |
| Stanford University | Stanford, CA | No | 1885 | Stanford University, officially Leland Stanford Junior University, is a private research university located in the census-designated place of Stanford, California, near the city of Palo Alto. The campus occupies 8,180 acres (3,310 hectares), among the largest in the United States, and enrolls over 17,000 students. Stanford is ranked among the top universities in the world. |
| University of California, Berkeley | Berkeley, CA | Yes | 1868 | The University of California, Berkeley (UC Berkeley, Berkeley, Cal, or California) is a public land-grant research university in Berkeley, California. Established in 1868 as the University of California, it is the state's first land-grant university and the first campus of the University of California system. Its fourteen colleges and schools offer over 350 degree programs and enroll some 31,000 undergraduate and 12,000 graduate students. Berkeley is ranked among the world's top universities. |
| Georgia Tech | Atlanta, GA | Yes | 1885 | The Georgia Institute of Technology, commonly referred to as Georgia Tech or, in the state of Georgia, as Tech, is a public research university and institute of technology in Atlanta, Georgia. It is part of the University System of Georgia and has satellite campuses in Savannah, Georgia; Metz, France; Athlone, Ireland; Shenzhen, China; and Singapore. |

## Common Commands

## Activating virtual environment
Whenever opening a new CLI:
```
$ source env/bin/activate
```

## Starting up the server
```
(env) $ python manage.py runserver
```
Shut down using ^C

## Installing new packages
```
(env) $ pip install <packages>
(env) $ pip freeze > requirement.txt
```

## Creating database migrations
After editing a model, create a migration and migrate the database:
```
(env) $ python manage.py makemigrations api
(env) $ python manage.py migrate api
```

## Running unit tests
```
(env) $ python manage.py test
```
You may also specify a specific app to test, a specific test file, a specific test case, or a specific test method:
```
(env) $ python manage.py test college
(env) $ python manage.py test college.tests
(env) $ python manage.py test college.tests.CollegeTestCase
(env) $ python manage.py test college.tests.CollegeTestCase.test_college_data
```

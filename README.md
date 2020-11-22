Python 3 required (anything)
Postgresql required at leat 10 version 
pip required

create virtual env 

1. Create a virtual environment named venv.

C:\> virtualenv %HOMEPATH%\path\to\app\catalog\venv

2. Activate the virtual environment.

C:\>%HOMEPATH%\path\to\app\catalog\venv\bin\activate

3. Install packages

pip install -r requirements.txt

4. Run Postgresql service

5. Make migrations
./manage.py migrate
lub
python manage.py migrate

6. Runserver by default on port 8000

./manage.py runserver
lub
python manage.py runserver

7. Api links

A. to logout
http://localhost:8000/api/user/logout/blacklist/

request type POST
body (only json)
{
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNjE1NTQwNCwianRpIjoiNDEyODBkZDQ1MzhkNGE5YzlhNzhlOGJjYzJhNjRkNGYiLCJ1c2VyX2lkIjoyfQ.JEkuFQhOVv4UuWB-2gM7vDB4ETMKT3OLLbZ0BUTotqs"
}

B. To login

API Link
http://localhost:8000/api/token/
Body link json:
{
    "email": "user2@user.com",
    "password": "user"
}

Response:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNjE1NTQwNCwianRpIjoiNDEyODBkZDQ1MzhkNGE5YzlhNzhlOGJjYzJhNjRkNGYiLCJ1c2VyX2lkIjoyfQ.JEkuFQhOVv4UuWB-2gM7vDB4ETMKT3OLLbZ0BUTotqs",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA2MDY5MzA0LCJqdGkiOiIyY2ZkNmQxODhlN2E0YmQxYWRjOGU5OWI3YmU4NDBkYyIsInVzZXJfaWQiOjJ9.HDfb_nah-4SydCHM4hsnO0eVakq4nx3O6KzxZmbyZP4"
}

C. Link to create user
http://localhost:8000/api/token/
{
    "email": "user3@user.com",
    "password": "user",
    "name":"user",
    "surname":"user",
    "phone_number" : "111222333",
    "birthdate" : "1111-11-11",
    "pesel" : "11111122333"
}
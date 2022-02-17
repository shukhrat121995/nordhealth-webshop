# NordHealth: Trial Work | WebShop

### Introduction
Simple and responsive website. Purely done in a Django Framework. Users will be able to look for a certain product by typing product names or codes in a search bar. Some AJAX calls were used in order to make
user interaction more comfortable and eye-catching. PostgreSQL was used in development mode. 

### Setup

To get this project up and running you should start by having Python installed on your computer. It's advised you create 
a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

**Note:** _you can use ```pipenv``` even though it is a bit slower than ```virtualenv```, it is quite comfortable and easy to use._

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:
```
source env/bin/active
```

Then install the project dependencies with
```
pip install -r requirements.txt
```

**Create a ```.env``` file inside the root directory. You need to have the following information inside your ```.env``` file:**
```
SECRET_KEY= <put your own secret key>

USER= <PostgreSQL user name>

PASSWORD= <PostgreSQL user password>
```

Run the database migrations with this command
```
python manage.py migrate
```

Now you can run the project with this command
```
python manage.py runserver
```
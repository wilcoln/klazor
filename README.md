# klazor
Klazor is a binder...
## Installation
```bash
git clone git@github.com:wilcoln/klazor.git
cd klazor
npm install
pip install -r requirements.txt
```

## Setup
You need to create a database and then specify it in the `settings.py` file as well as the database user credentials.
> NB: we recommend the use of **"klazor"** as the name of your database.

After that you have to run the following:
```bash
python manage.py migrate
python manage.py loaddata folders.json
python manage.py createsuperuser
```
## Run
```bash
python manage.py runserver
```
## Preview
![home](https://drive.google.com/uc?id=18yH2ABjyBAxsrVRSy20MwpKQbt4ev5Pb)
---
![sheet](https://drive.google.com/uc?id=1mop-XVh9RNJ2PVeGLEdG4VXvl6BfGrOR)

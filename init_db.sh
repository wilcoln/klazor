echo "drop database klazor;create database klazor;alter database klazor character set utf8mb4 collate utf8mb4_general_ci" | python manage.py dbshell
rm klazor/migrations/0001_initial.py
python manage.py makemigrations
python manage.py migrate
python manage.py seed
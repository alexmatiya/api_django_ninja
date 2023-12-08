# Данный проект создавался исключительно для ознакомления с DJANGO NINJA.

- Создал простенькое приложение с двумя модельками ЗАМЕТКА и КАТЕГОРИЯ через ОдинКоМногим. Подкрутил немного кривой:) фронт, сделал апишку через DJANGO NINJA.


- Кто захочет запустить, пользуемся стандартной процедурой:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
- После запуска, вам на главную или сюда:
```
http://localhost:8000/api/docs
```
или сюда
```
http://localhost:8000/admin
```

- p.s.: в зависимостях есть интересная библиотека ``django_extensions``, советую почитать про нее.
Запустите ``python manage.py shell_plus --print-sql``
и дерните что-то из базы, посмотрите, какая красота в терминале :)
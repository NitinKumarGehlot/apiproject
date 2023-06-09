## API PROJECT  

> _cscapp - application for countries, states, cities api_
---

#### How to run project

clone repository

```bash
python -m venv env
.\env\scripts\activate

cd apiproject
pip install -r requirements.txt
```

create a database 'apidatabase'
upload countries.sql , states.sql , cities.sql (from countries-states-cities-database-master\sql folder into your apidatabase)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# django-starter-bs4

Django example project with bootstrap 4 templates 
2 small apps with simple models, django forms and BS4 templating

## Installation

- create a virtualenv : `virtualenv -p python3 venv`
- install python dependencies : `pip install -r requirements.txt`
- activate : `source venv/bin/activate`
- migrate : `./manage.py migrate`
- install  static dependencies : `yarn newinstall ` (at root level)
    

## Run server

Just do:

`./manage.py runserver`


## Available routes 

```bash
admin/

lesTaches/home/<param> [name='home']
lesTaches/listing [name='listing']

contacts/ [name='contact']
contacts/detail/<int:cid> [name='detail']
contacts/edit/<int:pers_id> [name='edite']
contacts/del/<int:pers_id> [name='delete']
contacts/list [name='listing'] 
```

## or ... use gitpod 


[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/roza/django-starter-bs4)
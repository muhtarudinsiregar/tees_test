## Installation
 * git clone `https://github.com/muhtarudinsiregar/tees_test.git`
 * Install dependencies `pip install -r requirements.txt`
 * Create superuser or using current user:

    `username: ardin` and `password: superadmin`
 * run app `./manage.py runserver` and open your browser or postman/insomnia `localhost:8000`


## ENDPOINTS
* Login
```
GET /teams/:team_id/members
```

 * Get lists
```
GET /orders/
```

 * Store
```
POST /orders/

payload: size
type: string
```

 * Show detail
```
GET /orders/:id/
```

 * Update
```
PUT /orders/:id/

payload: size
type: string
```

 * Delete
```
DELETE /orders/:id/
```

## Run Tests
 * `./manage.py test`


## Packages
 * [Django Framework](https://github.com/django/django)
 * [Django REST Framework](https://github.com/encode/django-rest-framework)
 * [DRF JWT](https://github.com/GetBlimp/django-rest-framework-jwt)

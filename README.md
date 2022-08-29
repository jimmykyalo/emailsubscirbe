<h1 align="center">Welcome to Django Mailchimp Subscriber with React 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
</p>

> Django Mailchimp User Subscription form using the offial Mailchimp API. Froentend designed using React JS Framework and styled using Tailwind CSS 

### 🏠 [Homepage](https://github.com/jimmykyalo/emailsubscirbe)

### ✨ [Demo](https://mailchimpsubscriber.herokuapp.com/)

## Install

```sh
cd frontend
npm install
```
```sh
cd backend
pip install -r requirements.txt
```

## Usage

```sh
navigate to backend/base/views.py

update the part below with your: api_key, server prefix and list/audience id
mailchimp.set_config({
    "api_key": "exxxxxxxxxxxxxxb46beb55ea0-usxx",
    "server": "usxx"
    })

    list_id = "7b7dxxxxx" 
```


```sh
cd backend
python manage.py runserver
```

```sh
cd frontend
npm run start
```



## Author

👤 **Jimmy Kyalo**

* Website: https://github.com/jimmykyalo/
* Github: [@jimmykyalo](https://github.com/jimmykyalo)


# SocialStream

A social posting website built for influencers that want to interact with their community without a middle-man.  Crosspost from other platforms or post directly. It's Django/Python based with JS as needed. The architecture emphasizes speed and simplicity. 


## Installation

```bash
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
```

Copy local_settings.template to local_settings.py and customize.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Optionally you can fill the site with test data

```bash
python manage.py fille_data
```

## Screenshots

![socialstream screenshot A](https://github.com/adamhub/socialstream/raw/master/src/misc/ss1.jpg "Screeshot A")
![socialstream screenshot B](https://github.com/adamhub/socialstream/raw/master/src/misc/ss2.jpg "Screeshot B")
![socialstream screenshot D](https://github.com/adamhub/socialstream/raw/master/src/misc/ss3.jpg "Screeshot C")

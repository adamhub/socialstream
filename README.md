# SocialStream

In an age where you're hard work on social media can be shut down due to unfounded violations, owning your social media data and community is the best answer.

This is a self-hosted Social media hub built for influencers. It's like Facebook just for your community. Post videos and any other media or embeds, collect and connect with your community. Be available even if you are censored on other platforms. Control your own monetization. Keep in contact with your users even when shut down on other networks.

Ani-Censorship
This software is free for anyone to use, always. Since you can host it on your own server, no-one will censor you, unless your domain gets blacklisted at a high level. Even then, you can host your domain elsewhere, change your domain, password protect access, and many other things which keep you online. This platform aims to make all of these things easy.

## How SocialStream Compares

### vs Facebook
* Facebook can instantly block your account without notice, leaving your community in the lurch. 


### vs Wordpress
* Wordpress is a CMS first, and not great for community gathering


### vs Twitter
* You can be censored on twitter. 
* They use a secret algorithm for comments, posts, searches, hashtags, and it might be detrimental to your community. 
* Twitter is built to be addictive while ours is built to be informative and uplifting.

### vs Fediverse
* Fediverse is great, and we plan to integrate with it
* Pleroma/Mastodon (Fediverse platforms) and others are built with multi-tenency. Our focuses on single author usability first.
* The streams don't encourage elevated conversation and the UIs downplay conversation threads
* Complications arise with setup since Fediverse is complex to wrap your head around.



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

![socialstream screenshot A](/misc/ss1.jpg "Screeshot A")
![socialstream screenshot B](/misc/ss2.jpg "Screeshot B")
![socialstream screenshot D](/misc/ss3.jpg "Screeshot C")

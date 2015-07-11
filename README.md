# TadCall

Tadcall is a service that lets users to create discardable phone numbers that they can share.
Over these numbers you can then add restrictions, geographical, time or even number of received calls.

Tadcall allows you to regain countrol of your phone number:

 * You can see the live pitch: https://www.youtube.com/watch?v=HX-9SvpV6PI
 * And the presentation: http://www.slideshare.net/jtrindade/tadcall-presentation

Tadcall uses [Apidaze](http://apidaze.io) sdk and services on the backend. Thank you *Apidaze*.

# INSTALL:

 * sudo pip install Django
 * python manage.py migrate
 * cd tadcall && python manage.py startapp backend
 * python manage.py makemigrations backend
 * python manage.py migrate

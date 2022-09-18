CREATION GOAL
This mini-project was implemented to try using Celery for parallel task execution while using Redis as task broker.

It queues a task of getting a random cat image from URL https://cataas.com/cat, and downloading it to a local directory 
each time you open 0.0.0.0:8000 or hit refresh while on the page.

UPD: Updated the mini-project by adding django-celery-beats functionality, which allows to set up scheduled tasks for 
celery 

Tasks can be set up in admin panel - in our case it is set up to download pictures of cats every minute so sqlite DB file included
CREATION GOAL
This mini-project was implemented to try using Celery for parallel task execution while using Redis as task broker.

It queues a task of getting a random cat image from URL https://cataas.com/cat, and downloading it to a local directory 
each time you open 0.0.0.0:8000 or hit refresh while on the page.
  
# Learning Log 2.0

I followed a tutorial to create the Learning Log project
using Django 1.8 because I wanted to get the same results
as in the original project and get familiar with the
process. I posted that project in a diferent repository
called learning\_log18 for studies purposes.

This repository is the translation I did manually
from Django1.8 to Django2.0 to get familiar with the URL
syntax and other little details that Django2.0 has.
However, at the time I'm pushing this to github the most
recent version of Django is 2.2, which I couldn't test
because of my old hardware.

The process followed to convert the code from version 1.8
to 2.0 was the same as in the previous Learning Log
project. The following examples show the syntax to follow
for Django2.0

## URL File

There's no need to use regular expressions in Django2.0
to create urls for the web application in the urls.py
file. Here are some examples of the syntax:

```
path('topics/', views.topics, name='topics')
```

In order words:

```
path('posts/', views.posts, name='posts')
```

You must also add app\_name variable before the urlpatterns:
```
app_name = 'learning_logs'
```

Make sure to import **path** before creating urls:

```
from django.urls import path
```

If you are editing the urls.py located at the root of your
project, you must also use **include**:

```
from django.urls import path, include
```

Then the urlpattern for the home page would be:

```
path('', include('learning_logs.urls', namespace='learning_logs'))
```

## Views File

Django 2.0 removes the django.core.urlresolvers module. It
was moved to django.urls:

```
from django.urls import reverse
```

## Models File

If you are going to use the ForeignKey class within your
models, you must add on\_delete parameter:

```
topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
```

## Settings File

According to my research, the syntax used to activate your
apps in the settings.py at the section of INSTALLED\_APPS
file is as shown:

```
'learning_logs.apps.LearningLogsConfig'
```

The syntax is similar to what you can see in the apps.py
file in Django 2.0.

These were the most significant changes that coused a lot
of troubles while I was recreating Learning Log project.
Still it is recommended to keep studying the documentation
to be aware of the possible changes that developers may
do to newer Django versions.

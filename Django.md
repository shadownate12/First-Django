# The Django Web Application Framework

[https://www.djangoproject.com/](https://www.djangoproject.com/)

Django is a web application framework written in and using the Python programming language.

**IMPORTANT! when you search for Django resources online make sure they match the version of Django you have installed!**

The version of Django that we'll be using in this class is v4.1.x (the 3rd
component of the version number is not significant).   My plan is to stick with
version 4.1.x throughout the entire semester, even if a newer minor version is
released.

Official Documentation for our version of Django: [https://docs.djangoproject.com/en/4.1/](https://docs.djangoproject.com/en/4.1/)

## Table of Contents

*   [What is an Application Framework?](#what-is-an-application-framework)
*   [What does Django actually do?](#what-does-django-actually-do)
*   [Installing Django with `pip`](#installing-django-with-pip)
*   [Checking your version of Django](#checking-your-version-of-django)
*   [Creating your first Django project and app](#creating-your-first-django-project-and-app)
*   [What's the difference between a _project_ and an _app_?](#whats-the-difference-between-a-project-and-an-app)
*   [What are all of the files Django makes for me?](#what-are-all-of-the-files-django-makes-for-me)
*   [The Official Django Tutorial](#the-official-django-tutorial)
*   [Writing our first Django views](#writing-our-first-django-views)
*   [What is a template in Django?](#what-is-a-template-in-django)
*   [The Django template language](#the-django-template-language)
*   [What are Context Objects in Django?](#what-are-context-objects-in-django)
*   [Removing hard coded URLs in templates](#removing-hard-coded-urls-in-templates)
*   [How to include static content in a Django-generated page](#how-to-include-static-content-in-a-django-generated-page)
*   [What is MVC and/or MTV?](#what-is-mvc-andor-mtv)



## What is an Application Framework?

An application framework is software that provides a fundamental structure to
support the development of applications for a specific environment.


### Libraries vs. Frameworks

Software developers rely on pre-written collections of code to make their lives
easier.  We can separate these collections into two broad categories: libraries
and frameworks.


#### Library

A collection of classes, functions and variables which don't need to be used in
a particular way.  You have freedom to mix and match code from a library as you
see fit.

A library is a box of generic Legos(tm) which you can assemble in any way you wish.

![./assets/lego-library.jpg ](./assets/lego-library.jpg "You are limited only by your imagination!")


#### Framework

A collection of classes, functions and variables which imposes a particular
structure on your project.  A framework not only dictates which
files/classes/methods are to be used, but also where and when.  A framework
will suggest a "shape" for your project.

A framework is a specific Lego(tm) set meant to build a particular toy.

![./assets/lego-framework.jpg](./assets/lego-framework.jpg "You can build anything you want, so long as what you want is a Porg(tm)")


A framework:

-   Helps us build webapps quickly
-   Holds the rest of the application together
-   Provides and defines the shape of the application


Frameworks make use of the software architecture concept of "Inversion of control".  Put another way:

> The key difference between a library and a framework is "Inversion of
> Control".  When you call a method from a library, you are in control.
> But with a framework, the control is inverted: the framework calls you.
>
> -- https://www.programcreek.com/2011/09/what-is-the-difference-between-a-java-library-and-a-framework/


![In Soviet Russia, Framework calls you!](./assets/lib.vs.framework.png "In Soviet Russia, Framework calls you!")


### Django is an example of a framework

#### Django Pros

-   Django gives you a quicker route to your working app
-   It guides you as you make your app, choices are already made for you
-   Batteries are included


#### Django Cons

-   You give up a lot of control over how your project is organized
-   If your app isn't in Django's "shape", then Django gets in your way more than it helps
-   Sometimes what you want is a solar panel, not a battery



## What does Django actually do?

While you are in the process of developing your application Django provides you
with a basic web server and a simple database engine.  Once your application is
complete you would deploy your Django application into a "real" web server such
as Apache (httpd) or Nginx.

What do "real" web servers actually do?

### Static servers

Some web servers respond to HTTP requests by sending back a file attached to
HTTP headers.  Each identical request results in an identical response.  Static
web servers can be thought of as a mapping from URLs to local files.  Save for
small details like the "Date" header, the content of each response will always
be the same.

    $ nc unnovative.net 80
    GET /level1.html HTTP/1.0

    $ nc google.com 80
    GET /teapot HTTP/1.1

*You can think of a webpage served by a Static server as a __file__*


### Dynamic servers

Some web servers (such as your simple HTTP Server and Django) respond to HTTP
requests by calling a *function* which can return different content each time.

The webpage at http://checkip.dyndns.com returns a different HTML document
depending upon the IP address you visit from (not unlike the `/debug` page from
Assignment #1).

    $ nc checkip.dyndns.com 80
    GET / HTTP/1.1
    Host: checkip.dyndns.com
    Connection: close

This function's input is the entirety of the HTTP request, including the method
of the request (`GET`, `PUT`, `POST`, `DELETE`), the URL requested, all of the
HTTP headers as well as any data sent by the user agent.

This response can be *anything* that a function can compute from these inputs.
The function could return:

*   The contents of an HTML file found on the hard drive
*   A hard-coded string that contains an HTML document
*   A dynamically generated string which combines data from the HTTP
    request headers and `GET` request parameters
*   An HTML document generated by examining data `POST`ed from an HTML form
*   Information from weather sensors connected to the web server...
*   Pictures of lava lamps


*You can think of a webpage served by a Dynamic server as a __function__ that takes an HTTP request as input and returns an HTTP response*

Commonly, this *function* will utilize a *database* as part of its computation.


### Django is a framework for creating dynamic web servers

Django's entire reason for existing is to make it as easy as possible for you
to create a fully-functional dynamic web site that relies on a database for
storage.


## Installing Django with `pip`

Django is an ordinary Python package.  The easiest way to install it is to use
Python's built-in package manager `pip`.  You'll want to be sure that you've
installed Django for Python 3 and not for Python 2.  In the event that you have
two or more different versions of Python installed on your machine, use the
`pip3` command to make sure that all of the files are put into the right place.

The `--user` argument to pip's `install` subcommand installs files under your
home directory instead of `C:\Program Files` or `/usr/`.  This allows you to
run installs and updates without needing administrator privileges.

*Note: In the following commands you should run `python` instead of `python3` if that command does not exist on your computer.*


```bash
$ pip3 install --user django
```

If your computer tells you `pip3: Command not found`, you may install it this way:

```bash
$ python3 -m pip install --user django
```


## Checking your version of Django

You can check the version of Django that is installed with this command:

```bash
$ python3 -m django --version
```

The version of Django that we'll be using in this class is v4.1.x (the 3rd
component of the version number is not significant).   My plan is to stick with
version 4.1.x throughout the entire semester, even if a newer minor version is
released.

Official Documentation for our version of Django: [https://docs.djangoproject.com/en/4.1/](https://docs.djangoproject.com/en/4.1/)

### IMPORTANT!

**When you're looking up Django documentation, be sure that you're looking at documentation for the correct version of Django! (It's in the lower-right corner)**


## Creating your first Django project and app

The commands described in this section will get you up and running.

0.  Create a new Django Project called `cs2610proj` using the `django` module
    from the command line.  While the official tutorial instructs you to run
    the `django-admin` command, it is not correctly installed for all students,
    and the following command is 100% compatible:

    ```bash
    $ python3 -m django startproject cs2610proj
    ```

1.  Initialize a git repo in the newly-created project directory:

    ```bash
    $ cd cs2610proj
    $ git init
    ```

2.  **IMPORTANT** Create a `.gitignore` file with the following contents:

    ```
    db.sqlite3
    venv
    .DS_Store
    __pycache__
    *.pyc
    *.csv
    *.zip
    *.bak
    ```

3.  Commit your changes to git.

    ```bash
    $ git add .
    $ git status
    $ git commit -m "Created my Django project with a .gitignore file"
    ```

4.  Launch the Django development server so you can visit your project in your browser

    ```bash
    $ python3 manage.py runserver
    ```

5.  Visit http://127.0.0.1:8000 in your browser to see your new Django project
    in action.  Congratulations, you've just set up a working web server in
    Python without writing any code!

6.  Use `Ctrl-C` to stop the Django development server.

7.  Create a new Django app using your Django project's `manage.py` program

    ```bash
    $ python3 manage.py startapp hello
    ```




## What's the difference between a _project_ and an _app_?

We will use Django by creating a *project* which contains *apps*.

-   Project
    -   The code Django creates for me, containing my apps; a.k.a. my project directory
    -   Infrastructure: HTTP inputs and outputs, routing requests to different functions, etc.
    -   Configuration: allows my app to run under different Web Servers (i.e. Apache, Nginx)
    -   Development support: includes a simple HTTP server to support quick development

-   Apps
    -   The code I actually want to write
    -   The fun stuff my users will enjoy



## What are all of the files Django makes for me?

It is common for code frameworks to provide you with a bunch of *boilerplate* code.  Part of learning a framework is learning how to navigate and work within its structure.

#### Boilerplate code

> In computer programming, boilerplate code, or simply boilerplate, are sections of code that are repeated in multiple places with little to no variation. When using languages that are considered verbose, the programmer must write a lot of boilerplate code to accomplish only minor functionality.
>
> [Wikipedia: Boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code)

In Django, there are two categories of files that you will interact with: **project files** and **app files**.


#### Project files

The `python3 -m django startproject cs2610proj` command creates this directory structure:

```tree --charset=ascii
cs2610proj              Project directory; its name doesn't really matter
|-- cs2610proj          Project package; Django looks for settings in here.  The name of this directory matters!
|   |-- asgi.py         Pertains to the ASGI interface to a "real" web server
|   |-- __init__.py     Makes this directory importable as a Python module
|   |-- settings.py     Our project's settings
|   |-- urls.py         The "receptionist" - tells you where to go to use an app
|   `-- wsgi.py         Pertains to the WSGI interface to a "real" web server
`-- manage.py           Basically the same thing as django-admin, but customized to your project
```



#### App files

When we run `python3 manage.py startapp hello`, Django creates the skeleton of a
web application for us:

```tree --charset=ascii
cs2610proj
|-- cs2610proj
|-- manage.py
`-- hello
    |-- __init__.py     This file makes the 'hello' directory into a Python package
    |-- admin.py        Administration interface of your app
    |-- apps.py         Configuration information for the app
    |-- migrations/     Django generates scripts based on models.py in this director 
    |-- models.py       The 'M' in MVC     
    |-- views.py        The 'V' in MVC     
    |-- urls.py         The 'C' in MVC     
    `-- tests.py        Optional unit tests
```



Commit these files to Git as well:

```bash
$ git add hello
$ git commit -m "adding Django-generated 'hello' project"
```

#### Where should I place the `.gitignore` file?

Create your `.gitignore` in the *outer* `cs2610proj` directory so that it sits
right beside `manage.py`.  By placing it here it will prevent the database file
`db.sqlite3` file from being added and committed to your repository.


### All together, a Django project with one 'hello' app will look like this:

```tree --charset=ascii
cs2610proj              # Project directory; its name doesn't really matter
|-- .gitignore          # Avoid committing sensitive files!
|-- manage.py
|-- cs2610proj          # Project package; Django looks for settings in here.  The name of this directory matters!
|   |-- asgi.py         # Pertains to the ASGI interface to a "real" web server
|   |-- __init__.py     # Makes this directory importable as a Python module
|   |-- settings.py     # Our project's settings
|   |-- urls.py         # The "receptionist" - tells you where to go to use an app
|   `-- wsgi.py         # Pertains to the WSGI interface to a "real" web server
`-- hello
    |-- __init__.py     # This file makes the 'hello' directory into a Python package
    |-- admin.py        # Administration interface of your app
    |-- apps.py         # Configuration information for the app
    |-- migrations/     # Django generates scripts based on models.py in this director 
    |-- models.py       # The 'M' in MVC     
    |-- views.py        # The 'V' in MVC     
    |-- urls.py         # The 'C' in MVC     
    `-- tests.py        # Optional unit tests
```


## The Official Django Tutorial

One of Django's strongest advantages is the quality of its documentation.
When you have a question, please carefully read through the tutorial and the
other online resources.  While it's nice to have a teacher or a TA at your beck
and call, you must become self-sufficient sooner or later.  Now is the time for
you to learn how to answer your own questions by reading technical
documentation.

I did not just say *you are not allowed to ask me or the TAs questions about
Django*.  What I said is *when you ask your question, be ready for us to ask
"what did your own reading turn up?"*

The Django tutorial walks you through the creation of a Polls app.  Nearly
everything that you will need to know to complete the blog is learned through
this tutorial.  Consider the tutorial to be **required reading** and the polls
app to be part of this **assignment**.  I don't directly grade your polls app,
but the quality of your blog app will reflect the amount of effort you put into
doing this.

There are seven chapters in the Django tutorial, but you don't need to cover
all of them.  Material from the sections I ask you to read may appear on exams.


### Tutorial sections which I expect you to understand

-   [Part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
-   [Part 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)
-   [Part 3](https://docs.djangoproject.com/en/4.1/intro/tutorial03/)
-   [Part 4](https://docs.djangoproject.com/en/4.1/intro/tutorial04/) except for the last portion "Use generic views: Less code is better"
-   [Part 6](https://docs.djangoproject.com/en/4.1/intro/tutorial06/)


### Portions that you may safely skip over

-   [Part 4 section "Use generic views: Less code is better"](https://docs.djangoproject.com/en/4.1/intro/tutorial04/)
-   [Part 5 "Introducing automated testing"](https://docs.djangoproject.com/en/4.1/intro/tutorial05/)
-   [Part 7 "Customize the admin form"](https://docs.djangoproject.com/en/4.1/intro/tutorial07/)


## Writing our first Django views

https://docs.djangoproject.com/en/4.1/intro/tutorial01/#write-your-first-view

Django calls the functions which take HTTP requests as input and produce HTTP
responses as outputs *views*.  A Django webapp contains a file called
`views.py` in which these functions are written.

#### View (Django)
A Python function which takes an HTTP Request as input and returns an HTTP Response

A Django app may consist of many views, just as a Django project may consist of
many apps.  When Django receives an HTTP request how does it know which view to
call?  A system called the *controller* looks at each incoming request and
decides which view should handle it.



#### Controller (Django)
The part of Django which looks at an HTTP request and decides which view
function to call in response.


We configure the controller with a Python list called `urlpatterns` which
contains the directory for our project (e.g. directory like a phone book).
Django uses this list to decide which view function to call in response to
receiving a request for a URL.

The controller is like a receptionist in an office building.  When you want to
visit somebody at an office you ask the receptionist how to find that person.
They will then direct you where to go, or they might tell you that person is
temporarily unavailable.



### How do I configure the receptionists?

There are two receptionists in our Django office building:

* One on the main floor of the building (project) who directs traffic to the
  different floors in the building (apps).
* One on each floor (app) who directs traffic to specific people (views) in
  that office.

The controller is made up of files named `urls.py` in the project directory and
in each app directory.  The `urls.py` file under the project directory is
created by `python3 -m django startproj` command, and is already present.  A
source of confusion arises from the fact that when we run `manage.py startapp`,
Django doesn't make this file for us, and we must create it from scratch within
each app we make.


### What code should be in urls.py?

This file must contain a Python list (lists are equivalent to arrays in Python)
called `urlpatterns`.

The `urlpatterns` list contains `path` objects constructed with the `path()`
constructor.  Each `path` contains:

* A pattern describing part of the URL typed into the address bar of the client
* A function to call to serve the resource at this URL
* A name for this URL-to-function mapping

https://docs.djangoproject.com/en/4.1/intro/tutorial01/#path-argument-route

Once I set up my receptionists, Django will be able to run my view function
when I visit my app in a browser.




## What is a template in Django?

Basically we want to treat our HTML like a Wacky Mad Lib (TM) and fill in the
blanks.  A central feature of Django is the template system which lets us do
that, and so much more.  If you're familiar with Python's new *f-strings* this
will be very simple to pick up.


#### Template
Partially-formed webpage file with defined style and layout, containing regions
to be filled in programatically

https://docs.djangoproject.com/en/4.1/intro/tutorial03/#write-views-that-actually-do-something


Let's try this example again, but with templates.



### How Django loads templates

https://docs.djangoproject.com/en/4.1/topics/templates/#template-loading


### Install the template files

Create a subdirectory within your app named templates/, which itself contains
*another* subdirectory named for your app. For example, in my hello app I
create:

```bash
$ mkdir hello/templates
$ mkdir hello/templates/hello
```

Into this directory I place a template file named `index.html`.  This
convoluted scheme is to distinguish a template named `index.html` in my hello
app from another template called `index.html` in a different app.

An app with templates will have a file structure like this:

```tree --charset=ascii
cs2610proj
|-- .gitignore
|-- cs2610proj/
|-- manage.py
`-- hello
    |-- __init__.py     
    |-- admin.py        
    |-- apps.py         
    |-- migrations/     
    |-- models.py       
    |-- views.py        
    |-- urls.py         
    `-- templates/
        `-- hello/
            |-- index.html
            `-- highfive.html
```


### "Install" your app into the Django project

When a view asks to render a template Django will look for a directory called
`templates` in every *installed* app within the project.  You might think that
running `python3 manage.py startapp <APPNAME>` would be enough to install the
app, but it isn't.  We'll just have to do this part ourselves.

Django created many files for you When you started your app with the above
command.  One of the files was called `hello/apps.py`, which contains a Python
class that we must tell the Django project about.  This constitutes
"installing" our app.

These instructions are contained within the Django Tutorial, but I'll list them
here for your convenience as you follow along:

1.  Edit the Django project's `settings.py` file.
2.  Look for a variable named `INSTALLED_APPS`.  It is a Python list, where
    each element is a string giving the Pythonic name of classes corresponding
    to Django apps.
3.  Add to the list the Pythonic name of the class contained `hello/apps.py`.
    In my case, this string is `'hello.apps.HelloConfig'`.  Don't forget to add
    a comma after your string, or else you'll create a syntax error!


If you fail to install your app in this way, Django will fail to locate your
template file and you will see an error page bearing the error
`TemplateDoesNotExist`.



### Render the template in your view function

Next, in my view function, instead of returning an `HttpResponse` object
constructed with a string containing HTML content, I call the `render()`
function imported from the  `django.shortcuts` module.

`render()` needs two required arguments and can take a third optional argument.
These are:

1.  The HTTP request object which was passed to our view function
2.  A string naming our template file.  This name is a *relative path* which
    identifies the template under the `hello/templates` directory.  We leave
    out the part of the path containing our Django project, as well as the name
    of the `hello/templates` directory itself.
3.  *Optionally* a "context object" into which we put any variables that the
    template may use to fill-in the blanks.  If we don't pass a context object
    our template is effectively a static web page.


Here is a very minimal example:

```python
from django.shortcuts import render
from time import strftime

def index(request):
    context = { 'now' : strftime('%c')}
    return render(request, 'hello/index.html', context)
```




## The Django template language

https://docs.djangoproject.com/en/4.1/topics/templates/#the-django-template-language

Templates in Django are a mixture of HTML, CSS, etc. with markup that
Django looks for and acts upon. The Django template language has four
constructs:

#### `{{ Variables }}`

A variable outputs a value from the **context object**, which is a
dictionary-like object which maps *keys* to *values*.



#### `{% Tags %}`

Tags provide arbitrary logic in the rendering process. This can involve
conditionals (if/else blocks), loops (`{% for something in something %}`), etc.

https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#ref-templates-builtins-tags



#### `{# Comments #}`

Prevent text and markup from being rendered (e.g. `{# this won't be rendered #}`)

A `{% comment %}` tag provides multi-line comments.

```html
{% comment %}

    <!-- WIP: I haven't written the URLConf for 'some-url-name' yet,
    so this tag crashes right now  -->
    {% url 'some-url-name' v1 v2 %}

{% endcomment %}
```



#### `{{ textVariable | Filters }}`

Filters transform the values of variables and tag arguments.

https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#ref-templates-builtins-filters




## What are Context Objects in Django?

The data we send to the template renderer is packaged in a Python dictionary.

* [Python Intro: Dictionaries](https://usu.instructure.com/courses/474722/pages/dictionaries)
* [Official Python Tutorial: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries)

A dictionary is a compound datatype which is used like an array or list but
which uses strings in its subscript instead of integers.

* Lists in Python are constructed with `[]`
* Dictionaries in Python are constructed with `{}`

Lists are ordered collections of values. You look up items in a list by their
position.  You can meaningfully say "item x is before item y in this list".

Dictionaries, by contrast, are unordered collections of items.  There is no
concept of "before" or "after" when it comes to dictionaries.  Dictionaries are
key-value pairs.

Therefore, you don't store or retrieve data in a dictionary by referring to its
position.  Instead, you give each item a name, and refer to it thus.

A dictionary is denoted with curly braces `{ }`. Keys are separated from values
with a colon `:`.

```python
sculptors = {
        "light_fixtures": "Elsner",
        "concentric_arcs": "Ohran",
        "pivotal_concord": "Deming",
        "french_fries": "Kinnebrew",
        "Tools_of_Ag": ["Cummings","DeGraffenried"],
        "Whispers_and_Silence": "Suzuki",
        "PrincePhraApaimanee": "Kampalanont",
        "BlockA": "Be-No Club"
        }

print(sculptors['Whispers_and_Silence'])
```


## Removing hard coded URLs in templates

[Removing hard coded URLs in templates](https://docs.djangoproject.com/en/4.1/intro/tutorial03/#removing-hardcoded-urls-in-templates)

Instead of writing a hard coded URL which will suffer from the same drawbacks
as a hard coded absolute URL in a plain HTML file, we can get Django to write
the correct URL for us.  Use the `{% url %}` template tag to map the name of a
view function to a URL the browser can follow.  Then our template will always
work even if we change the mapping of URLs to view functions in the Controller.


## How to include static content in a Django-generated page

https://docs.djangoproject.com/en/4.1/intro/tutorial06/

Static content (CSS, images, JavaScript files) are to be placed in a
subdirectory named static/ under your app's directory. Just like with your
templates, you should create another subdirectory within static/ that matches
the name of your app.  For example:

```bash
$ mkdir hello/static
$ mkdir hello/static/hello
```

Files that are typically served statically include CSS style sheets, images,
and JavaScript programs.

An app with static files will have a structure like this:


```tree --charset=ascii
cs2610proj
|-- .gitignore
|-- cs2610proj/
|-- manage.py
`-- hello
    |-- __init__.py     
    |-- admin.py        
    |-- apps.py         
    |-- migrations/     
    |-- models.py       
    |-- views.py        
    |-- urls.py         
    |-- templates/
    |   `-- hello/
    |       |-- index.html
    |       `-- highfive.html
    `-- static/
        `-- hello/
            |-- family.jpg
            |-- portrait.png
            |-- script.js
            `-- style.css
```


The URL at which Django will make your static files available will not
necessarily match the directory structure of your web app, so it won't be wise
for you to try to hard code the URL to these resources into your template.

Rather, you will use the `{% static %}` tag to instruct the template renderer to
create the correct URL for you. While this does feel extraordinarily
complicated at first, it does give you the flexibility to later on move or
rename your app with a minimum of fuss.

Remember to use the `{% load static %}` tag the top of your template to enable
the `{% static %}` tag.


Example:

```html
{% load static %}
<html>
    <head>
        <title>How I shall take over the world</title>
        <link rel="stylesheet" href="{% static 'hello/style.css' %}">
    </head>
    <body>

        <!-- pretend there is content in here... -->

    </body>
</html>
```


## What is MVC and/or MTV?

When you learn about Django (and other web or GUI frameworks) you'll see the
acronyms MVC and MTV being bandied about. These describe a style means of
organization for an application's code. The idea is to identify the broad types
of things your code will do, and keep code with the same purpose together.

**MVC:** [Model, View, Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

-   **Model** - Data stored in some kind of database (in our case this is a
    SQLite database file named `db.sqlite3`)
    -   Configured in an app's `models.py` file.
    -   Also influenced by scripts found under the app's `migrations/` directory.
-   **View** - Presentation for the user (HTML, CSS, JavaScript; the things the
    user will see)
    -   Configured in an app's `views.py` file, and templates under
        `templates/<APP_NAME>`.
    -   Static files under `static/<APP_NAME>`
-   **Controller** - Transforms URLs into Views
    -   A list of `django.urls.path` objects called `urlpatterns`
    -   The controller for the entire Django project is configured in the file `<PROJ_DIR>/urls.py`
        -   think of a receptionist in an office building who directs you to the office you are seeking
    -   The controller for an app is configured in the file `<APP_DIR>/urls.py`.
        -   Contents of this file are *included* into the project's `<PROJ_DIR>/urls.py`

Django can be considered an MVC framework as your code can be divided into
these categories.  However, Django hackers prefer a different term (maybe they
want to be special?)

**MTV:** [Model, Template, View](https://docs.djangoproject.com/en/4.1/faq/general/#faq-mtv)

*Updated: Fri Mar 10 19:12:48 MST 2023*

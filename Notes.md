[TOC]

# A Complete Beginner's Guide to Django

## Part1 Getting Started

#### Introduction

![Welcome Class](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/Pixton_Comic_Welcome_Class.png)

Today I’m starting a new tutorial series about Django fundamentals. It’s a complete beginner’s guide to start learning Django. The material is divided into seven parts. We’re going to explore all the basic concepts in great detail, from installation, preparation of the development environment, models, views, templates, URLs to more advanced topics such as migrations, testing, and deployment.

I wanted to do something different. A tutorial that would be easy to follow, informative and fun to read. That was when I came up with the idea to create some comics along the text to illustrate some concepts and scenarios. I hope you enjoy the reading!

But before we start…

Back when I worked as a substitute professor in a university, I used to teach an introduction to web development discipline for the newcomer students in the Computer Science course. And I would always start new classes with this Confucius quote:

![Confucius Quote](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/Pixton_Comic_Confucius_Quote.png)

So, hands on! Don’t just read the tutorials. Let’s do it together! You will learn much more by doing and practicing.

------

#### Why Django?

Django is a Web framework written in Python. A Web framework is a software that supports the development of dynamic Web sites, applications, and services. It provides a set of tools and functionalities that solves many common problems associated with Web development, such as security features, database access, sessions, template processing, URL routing, internationalization, localization, and much more.

Using a Web framework, such as Django, enables us to develop secure and reliable Web applications very quickly in a standardized way, without having to reinvent the wheel.

So, what’s so special about Django? For starters, it’s a Python Web framework, which means you can benefit from wide a range of open source libraries out there. The [Python Package Index](https://pypi.python.org/pypi) repository hosts over **116K** packages (as per 6 of Sep. 2017). If you need to solve a specific problem, the chances are someone has already implemented a library for it.

Django is one of the most popular Web frameworks written in Python. It’s definitely the most complete, offering a wide range of features out-of-the-box, such as a standalone Web server for development and testing, caching, middleware system, ORM, template engine, form processing, interface with Python’s unit testing tools. Django also comes with *battery included*, offering built-in applications such as an authentication system, an administrative interface with automatically generated pages for CRUD operations, generation of syndication feeds (RSS/Atom), sitemaps. There’s even a Geographic Information System (GIS) framework built within Django.

The development of Django is supported by the [Django Software Foundation](https://www.djangoproject.com/foundation/), and it’s sponsored by companies like JetBrains and Instagram. Django has also been around for quite some time now. It’s under active development for more than 12 years now, proving to be a mature, reliable and secure Web framework.

##### Who’s Using Django?

It’s good to know who is using Django out there, so to have an idea what you can do with it. Among the biggest Web sites using Django we have: [Instagram](https://instagram.com/), [Disqus](https://disqus.com/), [Mozilla](https://www.mozilla.org/), [Bitbucket](https://bitbucket.org/), [Last.fm](https://www.last.fm/), [National Geographic](http://www.nationalgeographic.com/).

For more examples you can see the [Django Sites](https://www.djangosites.org/) database, they offer a list of over **5K** Django-powered Web sites.

By the way, last year, in the Django Under The Hood 2016 conference, Carl Meyer, a Django core developer, and Instagram employee, gave a talk on [how Instagram use Django at scale](https://www.youtube.com/watch?v=lx5WQjXLlq8) and how it supported their growth. It’s a one hour talk, but if you are interested in learning more, it was an entertaining talk.

------

#### Installation

The first thing we need to do is install some programs on our machine so to be able to start playing with Django. The basic setup consists of installing **Python**, **Virtualenv**, and **Django**.

![Basic Setup](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/Pixton_Comic_Basic_Setup.png)

Using virtual environments is not mandatory, but it’s highly recommended. If you are just getting started, it’s better to start with the right foot.

When developing Web sites or Web projects with Django, it’s very common to have to install external libraries to support the development. Using virtual environments, each project you develop will have its isolated environment. So the dependencies won’t clash. It also allows you to maintain in your local machine projects that run on different Django versions.

It’s very straightforward to use it, you will see!

##### Installing Python 3.6.2

The first thing we want to do is install the latest Python distribution, which is **Python 3.6.2**. At least it was, by the time I was writing this tutorial. If there’s a newer version out there, go with it. The next steps should remain more or less the same.

We are going to use Python 3 because the most important Python libraries have already been ported to Python 3 and also the next major Django version (2.x) won’t support Python 2 anymore. So Python 3 is the way to go.

Go to [www.python.org](https://python.org/) click on the Python 3.6.2 download page, scroll down until you see the download files listed below:

![Python 3.6.2 Windows Installer Download](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/download.png)

Pick the right version accordingly to your Windows distribution. If you are not sure which one is the right for you, the chances are you want to download the **Windows x86-64 executable installer** version.

Go to your Downloads directory, right click on the installer and click on **Run as administrator**.

![Run as administrator](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/run-as-admin.png)

Make sure you check the option **Add Python 3.6 to PATH** and click on the **Install Now** option.

![Install Now](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/install-python.png)

After the installation completes, you should see the following screen:

![Installation Successful](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/successful-installation.png)

Now search for the **Command Prompt** program and open it:

![Command Prompt](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/search-cmd.png)

To test if everything is working fine so far, type following command:

```
python --version
```

As an output you should see:

```
Python 3.6.2
```

![python --version](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/test-installation.png)

Great, Python is up and running. Next step: Virtual Environments!

##### Installing Virtualenv

配置一个虚拟环境[¶](https://docs.djangoproject.com/zh-hans/3.1/howto/windows/#setting-up-a-virtual-environment)

最佳实践是为你创建的每一个Django项目创建一个独立的环境。在Python生态系统中有许多可以用来管理环境和包的可选工具，一些在 [Python documentation](https://packaging.python.org/guides/tool-recommendations/) 被推荐过。我们将会在这份指南中使用Python本身自带的 [venv](https://docs.python.org/3/tutorial/venv.html) 来管理环境。

要为你的项目创建一个虚拟环境，打开新的命令行窗口，转至你想创建项目的文件夹，然后输入如下命令

```
...\> py -m venv project-name
```

这样就会创建一个名字为“project-name”文件夹并且设置好相应的虚拟环境。为了激活环境，请执行如下命令

```
...\> project-name\Scripts\activate.bat
```

虚拟环境就会激活，并且你会在命令提示符旁边看到 "(project-name)" 指向该环境。每次你打开新的命令行窗口，你需要再次激活环境。

For the next step, we are going to use **pip**, a tool to manage and install Python packages, to install **virtualenv**.

In the Command Prompt, execute the command below:

```
pip install virtualenv
```

![pip install virtualenv](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/pip-virtualenv.png)

So far the installations that we performed was system-wide. From now on, everything we install, including Django itself, will be installed inside a Virtual Environment.

Think of it like this: for each Django project you start, you will first create a Virtual Environment for it. It’s like having a sandbox for each Django project. So you can play around, install packages, uninstall packages without breaking anything.

I like to create a folder named **Development** on my personal computer. Then, I use it to organize all my projects and websites. But you can follow the next steps creating the directories wherever it feels right for you.

Usually, I start by creating a new folder with the project name inside my **Development** folder. Since this is going to be our very first project, we don’t need to pick a fancy name or anything. For now, we can call it **myproject**.

```
mkdir myproject
cd myproject
```

![Create myproject folder](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/myproject.png)

This folder is the higher level directory that will store all the files and things related to our Django project, including its virtual environment.

So let’s start by creating our very first virtual environment and installing Django.

Inside the **myproject** folder:

```
virtualenv venv
```

![Virtualenv](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/venv.png)

Our virtual environment is created. Now before we start using it, we need to activate:

```
venv\Scripts\activate
```

You will know it worked if you see **(venv)** in front of the command line, like this:

![Virtualenv activate](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/activate.png)

Let’s try to understand what happened here. We created a special folder named **venv**. It contains a copy of Python inside this folder. After we activated the **venv** environment, when we run the `python` command, it will use our local copy, stored inside **venv**, instead of the other one we installed earlier.

Another important thing is that the **pip** program is already installed as well, and when we use it to install a Python package, like Django, it will be installed *inside* the **venv** environment.

By the way, to deactivate the **venv** run the command below:

```
venv\Scripts\deactivate.bat
```

But let’s keep it activated for the next steps.

##### Installing Django 1.11.4

It’s very straightforward. Now that we have the **venv** activated, run the following command to install Django:

```
pip install django
```

![pip install django](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/windows/pip-django.png)

We are all set up now!

![End Installation](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/Pixton_Comic_End_Installation.png)

#### Starting a New Project

To start a new Django project, run the command below:

```
django-admin startproject myproject
```

The command-line utility **django-admin** is automatically installed with Django.

After we run the command above, it will generate the base folder structure for a Django project.

Right now, our **myproject** directory looks like this:

```
myproject/                  <-- higher level folder
 |-- myproject/             <-- django project folder
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/                  <-- virtual environment folder
```

Our initial project structure is composed of five files:

- **manage.py**: a shortcut to use the **django-admin** command-line utility. It’s used to run management commands related to our project. We will use it to run the development server, run tests, create migrations and much more.
- **__init__.py**: this empty file tells Python that this folder is a Python package.
- **settings.py**: this file contains all the project’s configuration. We will refer to this file all the time!
- **urls.py**: this file is responsible for mapping the routes and paths in our project. For example, if you want to show something in the URL `/about/`, you have to map it here first.
- **wsgi.py**: this file is a simple gateway interface used for deployment. You don’t have to bother about it. Just let it be for now.

Django comes with a simple web server installed. It’s very convenient during the development, so we don’t have to install anything else to run the project locally. We can test it by executing the command:

```
python manage.py runserver
```

For now, you can ignore the migration errors; we will get to that later.

Now open the following URL in a Web browser: **http://127.0.0.1:8000** and you should see the following page:

![It worked!](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/it-worked.png)

Hit CTRL + BREAK to stop the development server.

#### Django Apps

In the Django philosophy we have two important concepts:

- **app**: is a Web application that does something. An app usually is composed of a set of models (database tables), views, templates, tests.
- **project**: is a collection of configurations and apps. One project can be composed of multiple apps, or a single app.

It’s important to note that you can’t run a Django **app** without a **project**. Simple websites like a blog can be written entirely inside a single app, which could be named **blog** or **weblog** for example.

![Django Apps](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/Pixton_Comic_Django_Apps.png)

It’s a way to organize the source code. In the beginning, it’s not very trivial to determine what is an app or what is not. How to organize the code and so on. But don’t worry much about that right now! Let’s first get comfortable with Django’s API and the fundamentals.

Alright! So, to illustrate let’s create a simple Web Forum or Discussion Board. To create our first app, go to the directory where the **manage.py** file is and executes the following command:

```
django-admin startapp boards
```

Notice that we used the command **startapp** this time.

This will give us the following directory structure:

```
myproject/
 |-- myproject/
 |    |-- boards/                <-- our new django app!
 |    |    |-- migrations/
 |    |    |    +-- __init__.py
 |    |    |-- __init__.py
 |    |    |-- admin.py
 |    |    |-- apps.py
 |    |    |-- models.py
 |    |    |-- tests.py
 |    |    +-- views.py
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/
```

So, let’s first explore what each file does:

- **migrations/**: here Django store some files to keep track of the changes you create in the **models.py** file, so to keep the database and the **models.py** synchronized.
- **admin.py**: this is a configuration file for a built-in Django app called **Django Admin**.
- **apps.py**: this is a configuration file of the app itself.
- **models.py**: here is where we define the entities of our Web application. The models are translated automatically by Django into database tables.
- **tests.py**: this file is used to write unit tests for the app.
- **views.py**: this is the file where we handle the request/response cycle of our Web application.

Now that we created our first app, let’s configure our project to *use* it.

To do that, open the **settings.py** and try to find the `INSTALLED_APPS` variable:

**settings.py**

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

As you can see, Django already come with 6 built-in apps installed. They offer common functionalities that most Web applications need, like authentication, sessions, static files management (images, javascripts, css, etc.) and so on.

We will explore those apps as we progress in this tutorial series. But for now, let them be and just add our **boards** app to the list of `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'boards',
]
```

Using the analogy of the square and circles from the previous comic, the yellow circle would be our **boards** app, and the **django.contrib.admin**, **django.contrib.auth**, etc, would be the red circles.

------

#### Hello, World!

Let’s write our first **view**. We will explore it in great detail in the next tutorial. But for now, let’s just experiment how it looks like to create a new page with Django.

Open the **views.py** file inside the **boards** app, and add the following code:

**views.py**

```
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')
```

Views are Python functions that receive an `HttpRequest` object and returns an `HttpResponse` object. Receive a *request* as a parameter and returns a *response* as a result. That’s the flow you have to keep in mind!

So, here we defined a simple view called **home** which simply returns a message saying **Hello, World!**.

Now we have to tell Django *when* to serve this view. It’s done inside the **urls.py** file:

**urls.py**

```
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
```

If you compare the snippet above with your **urls.py** file, you will notice I added the following new line: `url(r'^$', views.home, name='home')` and imported the **views** module from our app **boards** using `from boards import views`.

As I mentioned before, we will explore those concepts in great detail later on.

But for now, Django works with **regex** to match the requested URL. For our **home** view, I’m using the `^$` regex, which will match an empty path, which is the homepage (this url: **http://127.0.0.1:8000**). If I wanted to match the URL **http://127.0.0.1:8000/homepage/**, my url would be: `url(r'^homepage/$', views.home, name='home')`.

Let’s see what happen:

```
python manage.py runserver
```

In a Web browser, open the http://127.0.0.1:8000 URL:

![Hello, World!](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/hello-world.png)

That’s it! You just created your very first view.

------

#### Conclusions

That was the first part of this tutorial series. In this tutorial, we learned how to install the latest Python version and how to setup the development environment. We also had an introduction to virtual environments and started our very first Django project and already created our initial app.

I hope you enjoyed the first part! The second part is coming out next week, on Sep 11, 2017. It’s going to be about models, views, templates, and URLs. We will explore together all the Django fundamentals! If you would like to get notified when the second part is out, you can [subscribe to our mailing list](https://colossus.simpleisbetterthancomplex.com/subscribe/d2320a41-0378-4aa8-8f4e-5bb1ffcd521d/).

Just so we can stay on the same page, I made the source code available on GitHub. The current state of the project can be found under the release tag **v0.1-lw**. The link below will take you to the right place:

https://github.com/sibtc/django-beginners-guide/tree/v0.1-lw

------

[![A Complete Beginner's Guide to Django - Index](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/featured.jpg)← Tutorial Series Index](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)

[![A Complete Beginner's Guide to Django - Part 2](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/featured.jpg)Part 2 - Fundamentals →](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)

## Part 2 Foundamentals

#### Introduction

Welcome to the second part of our Django Tutorial! In the previous lesson, we installed everything that we needed. Hopefully, you are all setup with Python 3.6 installed and Django 1.11 running inside a Virtual Environment. We already created the project we are going to play around. In this lesson, we are going to keep writing code in the same project.

In the next section, we are going to talk a little bit about the project we are going to develop, so to give you some context. Then after that, you are going to learn all the Django fundamentals: models, admin, views, templates, and URLs.

Hands on!

------

#### Web Board Project

I don’t know about you, but personally, I learn much more by seeing practical examples and code snippets. For me, it’s difficult to process a concept where in the examples you read `Class A` and `Class B`, or when I see the classical `foo(bar)` examples. I don’t want to do that with you.

So, before we get into the fun part, playing with models, views, and everything. Let’s just take a moment and discuss very briefly about this project we are going to develop.

If you already have experience with Web development and feel it’s too much detail, you can just skim through the pictures to have an idea what we are going to build and then jump to the **Models** section of this tutorial.

But if you are new to Web development, I highly suggest that you keep reading. It will give you some good insights on modeling and design of Web applications. Web development, and software development in general, is not just about coding.

![Rocket Science](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/Pixton_Comic_Rocket_Science.png)

##### Use Case Diagram

Our project is a discussion board (a forum). The whole idea is to maintain several **boards**, which will behave like categories. Then, inside a specific board, a user can start a new discussion by creating a new **topic**. In this topic, other users can engage in the discussion posting replies.

We will need to find a way to differentiate a regular user from an admin user because only the admins are supposed to create new boards. Below, an overview of our main use cases and the role of each type of user:

![Use Case Diagram](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/use-case-diagram.png)

Figure 1: Use case diagram of the core functionalities offered by the Web Board

##### Class Diagram

From the Use Case Diagram, we can start thinking concerning the **entities** of our project. The entities are the models we will create, and it’s very closely related to the data our Django app will process.

For us to be able to implement the use cases described in the previous section, we will need to implement at least the following models: **Board**, **Topic**, **Post**, and **User**.

![Basic Class Diagram](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/basic-class-diagram.png)

Figure 2: Draft of the class diagram of the Web Board

It’s also important to take the time to think about how do models will relate to each other. What the solid lines are telling us is that, in a **Topic**, we will need to have a field to identify which **Board** it belongs to. Similarly, the **Post** will need a field to represent which **Topic** it belongs so that we can list in the discussions only **Posts** created within a specific **Topic**. Finally, we will need fields in both the **Topic** to know who started the discussion and in the **Post** so we can identify who is posting the reply.

We could also have an association with the **Board** and the **User** model, so we could identify who created a given **Board**. But this information is not relevant for the application. There are other ways to track this information, you will see later on.

Now that we have the basic class representation, we have to think what kind of information each of those models will carry. This sort of thing can get complicated very easily. So try to focus on the important bits. The information that you need to start the development. Later on, we can improve the model using **migrations**, which you will see in great detail in the next tutorial.

But for now, this would be a basic representation of our models’ fields:

![Class Diagram](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram.png)

Figure 3: Class diagram emphasizing the relationship between the classes (models)

This class diagram has the emphasis on the relationship between the models. Those lines and arrows will eventually be translated into fields later on.

For the **Board** model, we will start with two fields: **name** and **description**. The **name** field has to be unique, so to avoid duplicated board names. The **description** is just to give a hint of what the board is all about.

The **Topic** model will be composed of four fields: **subject**, **last update** date which will be used to define the topics ordering, **topic starter** to identify the **User** who started the **Topic**, and a field called **board** to define which **Board** a specific **Topic** belongs to.

The **Post** model will have a **message** field, which will be used to store the text of the post replies, a **created at** date and time field mainly used to order the **Posts** within a **Topic**, an **updated at** date and time field to inform the **Users** when and if a given **Post** has been edited. Like the date and time fields, we will also have to reference the **User** model: **created by** and **updated by**.

Finally, the **User** model. In the class diagram, I only mentioned the fields **username**, **password**, **email** and **is superuser** flag because that’s pretty much all we are going to use for now. It’s important to note that we won’t need to create a **User** model because Django already comes with a built-in **User** model inside the **contrib** package. We are going to use it.

Regarding the multiplicity in the class diagram (the numbers `1`, `0..*`, etc.), here’s how you read it:

![Class Diagram Board and Topic Association](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-board-topic.png)A **Topic** must be associated with exactly one (`1`) **Board** (which means it cannot be null), and a **Board** may be associated with many **Topics** or none (`0..*`). Which means a **Board** may exist without a single **Topic**.

![Class Diagram Topic and Post Association](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-topic-post.png)A **Topic** should have at least one **Post** (the starter **Post**), and it may also have many **Posts** (`1..*`). A **Post** must be associated with one, and only one **Topic** (`1`).

![Class Diagram Topic and User Association](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-topic-user.png)A **Topic** must have one, and only one **User** associated with: the topic starter **User** (`1`). And a **User** may have many or none **Topics** (`0..*`).

![Class Diagram Post and User Association](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-post-user.png)A **Post** must have one, and only one **User** associated with: **created by** (`1`). A **User** may have many or none **Posts** (`0..*`). The second association between **Post** and **User** is a *direct association* (see the arrow at the end of the line), meaning we are interested only in one side of the relationship which is what **User** has edited a given **Post**. It will be translated into the **updated by** field. The multiplicity says `0..1`, meaning the **updated by** field may be null (the **Post** wasn’t edited) and at most may be associated with only one **User**.

Another way to draw this class diagram is emphasizing the fields rather than in the relationship between the models:

![Class Diagram Attributes](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-attributes.png)

Figure 4: Class diagram emphasizing the attributes (fields) of the classes (models)

The representation above is equivalent to the previous one, and it’s also closer to what we are going to design using the Django Models API. In this representation, we can see more clearly that in the **Post** model the associations **topic**, **created by**, and **updated by** became model fields. Another interesting thing to note is that in the **Topic** model we have now an *operation* (a class method) named **posts()**. We are going to achieve this by implementing a reverse relationship, where Django will automatically execute a query in the database to return a list of all the **Posts** that belongs to a specific **Topic**.

Alright, enough UML for now! To draw the diagrams presented in this section I used the [StarUML](http://staruml.io/) tool.

##### Wireframes

After spending some time designing the application models, I like to create some wireframes to define what needs to be done and also to have a clear picture of where we are going.

![Wireframes Comic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/Pixton_Comic_Wireframes.png)

Then based on the wireframes we can gain a deeper understanding of the entities involved in the application.

First thing, we need to show all the boards in the homepage:

![Wireframe Boards](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/wireframe-boards.png)

Figure 5: Boards project wireframe homepage listing all the available boards.

If the user clicks on a link, say in the Django board, it should list all the topics:

![Wireframe Topics](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/wireframe-topics.png)

Figure 6: Boards project wireframe listing all topics in the Django board.

Here we have two main paths: either the user clicks on the “new topic” button to create a new topic, or the user clicks on a topic to see or engage in a discussion.

The “new topic” screen:

![Wireframe New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/wireframe-new-topic.png)

Figure 7: New topic screen

Now the topic screen, displaying the posts and discussions:

![Wireframe Posts](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/wireframe-posts.png)

Figure 8: Topic posts listing screen

If the user clicks on the reply button, they will see the screen below, with a summary of the posts in reverse order (newest first):

![Wireframe Reply](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/wireframe-reply.png)

Figure 9: Reply topic screen

To draw your wireframes you can use the [draw.io](https://draw.io/) service, it’s free.

------

#### Models

The models are basically a representation of your application’s database layout. What we are going to do in this section is create the Django representation of the classes we modeled in the previous section: **Board**, **Topic**, and **Post**. The **User** model is already defined inside a built-in app named **auth**, which is listed in our `INSTALLED_APPS` configuration under the namespace **django.contrib.auth**.

We will do all the work inside the **boards/models.py** file. Here is how we represent our class diagram (see [Figure 4](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html#figure-4)). in a Django application:

```python
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
```

All models are subclass of the **django.db.models.Model** class. Each class will be transformed into *database tables*. Each field is represented by instances of **django.db.models.Field** subclasses (built-in Django core) and will be translated into *database columns*.

The fields `CharField`, `DateTimeField`, etc., are all subclasses of **django.db.models.Field** and they come included in the Django core – ready to be used.

Here we are only using `CharField`, `TextField`, `DateTimeField`, and `ForeignKey` fields to define our models. But Django offers a wide range of options to represent different types of data, such as `IntegerField`, `BooleanField`, `DecimalField`, and many others. We will refer to them as we need.

Some fields have required arguments, such as the `CharField`. We should always set a `max_length`. This information will be used to create the database column. Django needs to know how big the database column needs to be. The `max_length` parameter will also be used by the Django Forms API, to validate user input. More on that later.

In the `Board` model definition, more specifically in the `name` field, we are also setting the parameter `unique=True`, as the name suggests, it will enforce the uniqueness of the field at the database level.

In the `Post` model, the `created_at` field has an optional parameter, the `auto_now_add` set to `True`. This will instruct Django to set the current date and time when a `Post` object is created.

==One way to create a relationship between the models is by using the `ForeignKey` field. It will create a link between the models and create a proper relationship at the database level. The `ForeignKey` field expects a positional parameter with the reference to the model it will relate to==.

For example, in the `Topic` model, the `board` field is a `ForeignKey` to the `Board` model. It is telling Django that a `Topic` instance relates to only one `Board` instance. The `related_name` parameter will be used to create a *reverse relationship* where the `Board` instances will have access a list of `Topic` instances that belong to it.

Django automatically creates this reverse relationship – the `related_name` is optional. But if we don’t set a name for it, Django will generate it with the name: `(class_name)_set`. For example, in the `Board` model, the `Topic` instances would be available under the `topic_set` property. Instead, we simply renamed it to `topics`, to make it feel more natural.

==In the `Post` model, the `updated_by` field sets the `related_name='+'`. This instructs Django that we don’t need this reverse relationship, so it will ignore it==.

Below you can see the comparison between the class diagram and the source code to generate the models with Django. The green lines represent how we are handling the reverse relationships.

![Class Diagram Models Definition](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/class-diagram-django-models.png)

At this point, you may be asking yourself: “what about primary keys/IDs”? If we don’t specify a primary key for a model, Django will automatically generate it for us. So we are good for now. In the next section, you will see better how it works.

##### Migrating the Models

The next step is to tell Django to create the database so we can start using it.

==Open the , activate the virtual environment, go to the folder where the **manage.py** file is, and run the commands below:==

```python
python manage.py makemigrations
```

As an output you will get something like this:

```
Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Board
    - Create model Post
    - Create model Topic
    - Add field topic to post
    - Add field updated_by to post
```

At this point, Django created a file named **0001_initial.py** inside the **boards/migrations** directory. It represents the current state of our application’s models. In the next step, Django will use this file to create the tables and columns.

==The migration files are translated into SQL statements. If you are familiar with SQL, you can run the following command to inspect the SQL instructions that will be executed in the database:==

```
python manage.py sqlmigrate boards 0001
```

If you’re not familiar with SQL, don’t worry. We won’t be working directly with SQL in this tutorial series. All the work will be done using just the Django ORM, which is an abstraction layer that communicates with the database.

==The next step now is to *apply* the migration we generated to the database:==

```
python manage.py migrate
```

The output should be something like this:

```
Operations to perform:
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying boards.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Because this is the first time we are migrating the database, the `migrate` command also applied the existing migration files from the Django contrib apps, listed in the `INSTALLED_APPS`. This is expected.

The line `Applying boards.0001_initial... OK` is the migration we generated in the previous step.

That’s it! Our database is ready to be used.

![SQLite](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/Pixton_Comic_SQLite.png)

 **Note:** It's important to note that **SQLite** is a production-quality database. SQLite is used by many companies across thousands of products, like all Android and iOS devices, all major Web browsers, Windows 10, macOS, etc.

It's just not suitable for all cases. SQLite doesn't compare with databases like MySQL, PostgreSQL or Oracle. High-volume websites, write-intensive applications, very large datasets, high concurrency, are some situations that will eventually result in a problem by using SQLite.

We are going to use SQLite during the development of our project because it's convenient and we won't need to install anything else. When we deploy our project to production, we will switch to PostgreSQL. For simple websites this work fine. But for complex websites, it's advisable to use the same database for development and production.

##### Experimenting with the Models API

One of the great advantages of developing with Python is the interactive shell. I use it all the time. It’s a quick way to try things out and experiment libraries and APIs.

==You can start a Python shell with our project loaded using the **manage.py** utility:==

```
python manage.py shell
```

This is very similar to calling the interactive console just by typing `python`, except when we use `python manage.py shell`, we are adding our project to the `sys.path` and loading Django. That means we can import our models and any other resource within the project and play with it.

Let’s start by importing the **Board** class:

```
from boards.models import Board
```

To create a new board object, we can do the following:

```
board = Board(name='Django', description='This is a board about Django.')
```

To persist this object in the database, we have to call the `save` method:

```
board.save()
```

==The `save` method is used both to *create* and *update* objects==. Here Django created a new object because the **Board** instance had no **id**. After saving it for the first time, Django will set the id automatically:

```
board.id
1
```

You can access the rest of the fields as Python attributes:

```
board.name
'Django'
board.description
'This is a board about Django.'
```

==To update a value we could do==:

```
board.description = 'Django discussion board.'
board.save()
```

==Every Django model comes with a special attribute; we call it a **Model Manager**. You can access it via the Python attribute `objects`. It is used mainly to execute queries in the database==. For example, we could use it to directly create a new **Board** object:

```
board = Board.objects.create(name='Python', description='General discussion about Python.')
board.id
2
board.name
'Python'
```

==So, right now we have two boards. We can use the `objects` to list all existing boards in the database:==

```
Board.objects.all()
<QuerySet [<Board: Board object>, <Board: Board object>]>
```

The result was a **QuerySet**. We will learn more about that later on. Basically, it’s a list of objects from the database. We can see that we have two objects, but we can only read **Board object**. That’s because we haven’t defined the `__str__` method in the **Board** model.

==The `__str__` method is a String representation of an object==. We can use the board name to represent it.

First, exit the interactive console:

```
exit()
```

Now edit the **models.py** file inside the **boards** app:

```
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

Let’s try the query again. Open the interactive console again:

```
python manage.py shell
from boards.models import Board

Board.objects.all()
<QuerySet [<Board: Django>, <Board: Python>]>
```

Much better, right?

We can treat this **QuerySet** like a list. Let’s say we wanted to iterate over it and print the description of each board:

```
boards_list = Board.objects.all()
for board in boards_list:
    print(board.description)
```

The result would be:

```
Django discussion board.
General discussion about Python.
```

==Similarly, we can use the model **Manager** to query the database and return a single object==. For that we use the `get` method:

```
django_board = Board.objects.get(id=1)

django_board.name
'Django'
```

But we have to be careful with this kind of operation. If we try to get an object that doesn’t exist, for example, a board with `id=3`, it will raise an exception:

```
board = Board.objects.get(id=3)

boards.models.DoesNotExist: Board matching query does not exist.
```

We can use the `get` method with any model field, but preferably use a field that can uniquely identify an object. Otherwise, the query may return more than one object, which will cause an exception.

```
Board.objects.get(name='Django')
<Board: Django>
```

Note that the query is *case sensitive*, a lower case “django” would not match:

```
Board.objects.get(name='django')
boards.models.DoesNotExist: Board matching query does not exist.
```

##### ==Summary of Model’s Operations==

Find below a summary of the methods and operations we learned in this section, using the **Board** model as a reference. Uppercase **Board** refers to the class, lowercase **board** refers to an instance (or object) of the **Board** model class:

| Operation                                  | Code sample                                           |
| :----------------------------------------- | :---------------------------------------------------- |
| Create an object without saving            | `board = Board()`                                     |
| Save an object (create or update)          | `board.save()`                                        |
| Create and save an object in the database  | `Board.objects.create(name='...', description='...')` |
| List all objects                           | `Board.objects.all()`                                 |
| Get a single object, identified by a field | `Board.objects.get(id=1)`                             |

In the next section, we are going to start writing views and displaying our boards in HTML pages.

------

#### Views, Templates, and Static Files

At the moment we already have a view named `home` displaying “Hello, World!” in the homepage of our application.

**myproject/urls.py**

```
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
```

**boards/views.py**

```
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')
```

We can use this as our starting point. If you recall our wireframes, the [Figure 5](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html#figure-5) showed how the homepage should look like. What we want to do is display a list of boards in a table alongside with some other information.

The first thing to do is import the **Board** model and list all the existing boards:

**boards/views.py**

```
from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
```

And the result would be this simple HTML page:

![Boards Homepage HttpResponse](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-httpresponse.png)

But let’s stop right here. We are not going very far rendering HTML like this. For this simple view, all we need is a list of boards; then the rendering part is a job for the **Django Template Engine**.

##### Django Template Engine Setup

Create a new folder named **templates** alongside with the **boards** and **mysite** folders:

```
myproject/
 |-- myproject/
 |    |-- boards/
 |    |-- myproject/
 |    |-- templates/   <-- here!
 |    +-- manage.py
 +-- venv/
```

Now within the **templates** folder, create an HTML file named **home.html**:

**templates/home.html**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}

  </body>
</html>
```

In the example above we are mixing raw HTML with some special tags `{% for ... in ... %}` and `{{ variable }}`. They are part of the Django Template Language. The example above shows how to iterate over a list of objects using a `for`. The `{{ board.name }}` renders the name of the board in the HTML template, generating a dynamic HTML document.

==Before we can use this HTML page, we have to tell Django where to find our application’s templates==.

==Open the **settings.py** inside the **myproject** directory and search for the `TEMPLATES` variable and set the `DIRS` key to `os.path.join(BASE_DIR, 'templates')`:==

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Basically what this line is doing is finding the full path of your project directory and appending “/templates” to it.

We can debug this using the Python shell:

```python
python manage.py shell
from django.conf import settings

settings.BASE_DIR
'/Users/vitorfs/Development/myproject'

import os

os.path.join(settings.BASE_DIR, 'templates')
'/Users/vitorfs/Development/myproject/templates'
```

See? It’s just pointing to the **templates** folder we created in the previous steps.

Now we can update our **home** view:

**boards/views.py**

```python
from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
```

The resulting HTML:

![Boards Homepage render](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-render.png)

We can improve the HTML template to use a table instead:

**templates/home.html**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    <table border="1">
      <thead>
        <tr>
          <th>Board</th>
          <th>Posts</th>
          <th>Topics</th>
          <th>Last Post</th>
        </tr>
      </thead>
      <tbody>
        {% for board in boards %}
          <tr>
            <td>
              {{ board.name }}<br>
              <small style="color: #888">{{ board.description }}</small>
            </td>
            <td>0</td>
            <td>0</td>
            <td></td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>
```

![Boards Homepage render](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-render-2.png)

##### Testing the Homepage

![Testing Comic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/Pixton_Comic_Testing.png)

This is going to be a recurrent subject, and we are going to explore together different concepts and strategies throughout the whole tutorial series.

Let’s write our first test. For now, we will be working in the **tests.py** file inside the **boards** app:

**boards/tests.py**

```python
from django.urls import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
```

This is a very simple test case but extremely useful. We are testing the *status code* of the response. The status code 200 means **success**.

We can check the status code of the response in the console:

![Response 200](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/test-homepage-view-status-code-200.png)

If there were an uncaught exception, syntax error, or anything, Django would return a status code **500** instead, which means **Internal Server Error**. Now, imagine our application has 100 views. If we wrote just this simple test for all our views, with just one command, we would be able to test if all views are returning a success code, so the user does not see any error message anywhere. Without automate tests, we would need to check each page, one by one.

To execute the Django’s test suite:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.041s

OK
Destroying test database for alias 'default'...
```

Now we can test if Django returned the correct view function for the requested URL. This is also a useful test because as we progress with the development, you will see that the **urls.py** module can get very big and complex. The URL conf is all about resolving regex. There are some cases where we have a very permissive URL, so Django can end up returning the wrong view function.

Here’s how we do it:

**boards/tests.py**

```python
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
```

==In the second test, we are making use of the `resolve` function. Django uses it to match a requested URL with a list of URLs listed in the **urls.py** module==. This test will make sure the URL `/`, which is the root URL, is returning the home view.

Test it again:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.027s

OK
Destroying test database for alias 'default'...
```

To see more detail about the test execution, set the **verbosity** to a higher level:

```
python manage.py test --verbosity=2
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying boards.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_home_url_resolves_home_view (boards.tests.HomeTests) ... ok
test_home_view_status_code (boards.tests.HomeTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.017s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```

Verbosity determines the amount of notification and debug information that will be printed to the console; 0 is no output, 1 is normal output, and 2 is verbose output.

##### Static Files Setup

==Static files are the CSS, JavaScripts, Fonts, Images, or any other resources we may use to compose the user interface==.

As it is, Django doesn’t serve those files. Except during the development process, so to make our lives easier. But Django provides some features to help us manage the static files. Those features are available in the **django.contrib.staticfiles** application already listed in the `INSTALLED_APPS` configuration.

With so many front-end component libraries available, there’s no reason for us keep rendering basic HTML documents. We can easily add Bootstrap 4 to our project. Bootstrap is an open source toolkit for developing with HTML, CSS, and JavaScript.

In the project root directory, alongside with the **boards**, **templates**, and **myproject** folders, create a new folder named **static**, and within the **static** folder create another one named **css**:

```
myproject/
 |-- myproject/
 |    |-- boards/
 |    |-- myproject/
 |    |-- templates/
 |    |-- static/       <-- here
 |    |    +-- css/     <-- and here
 |    +-- manage.py
 +-- venv/
```

Go to [getbootstrap.com](https://getbootstrap.com/docs/4.0/getting-started/download/#compiled-css-and-js) and download the latest version:

![Bootstrap Download](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/bootstrap-download.png)

Download the **Compiled CSS and JS** version.

In your computer, extract the **bootstrap-4.0.0-beta-dist.zip** file you downloaded from the Bootstrap website, copy the file **css/bootstrap.min.css** to our project’s css folder:

```
myproject/
 |-- myproject/
 |    |-- boards/
 |    |-- myproject/
 |    |-- templates/
 |    |-- static/
 |    |    +-- css/
 |    |         +-- bootstrap.min.css    <-- here
 |    +-- manage.py
 +-- venv/
```

==The next step is to instruct Django where to find the static files. Open the **settings.py**, scroll to the bottom of the file and just after the `STATIC_URL`, add the following==:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

Same thing as the `TEMPLATES` directory, remember?

Now we have to load the static files (the Bootstrap CSS file) in our template:

**templates/home.html**

```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <!-- body suppressed for brevity ... -->
  </body>
</html>
```

==First we load the Static Files App template tags by using the `{% load static %}` in the beginning of the template==.

==The template tag `{% static %}` is used to compose the URL where the resource lives.== In this case, the `{% static 'css/bootstrap.min.css' %}` will return **/static/css/bootstrap.min.css**, which is equivalent to **http://127.0.0.1:8000/static/css/bootstrap.min.css**.

The `{% static %}` template tag uses the `STATIC_URL` configuration in the **settings.py** to compose the final URL. For example, if you hosted your static files in a subdomain like **https://static.example.com/**, we would set the `STATIC_URL=https://static.example.com/` then the `{% static 'css/bootstrap.min.css' %}` would return **https://static.example.com/css/bootstrap.min.css**.

If none of this makes sense for you at the moment, don’t worry. ==Just remember to use the `{% static %}` whenever you need to refer to a CSS, JavaScript or image file==. Later on, when we start working with Deployment, we will discuss more it. For now, we are all set up.

Refreshing the page **127.0.0.1:8000** we can see it worked:

![Boards Homepage Bootstrap](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-bootstrap.png)

Now we can edit the template so to take advantage of the Bootstrap CSS:

```css
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item active">Boards</li>
      </ol>
      <table class="table">
        <thead class="thead-inverse">
          <tr>
            <th>Board</th>
            <th>Posts</th>
            <th>Topics</th>
            <th>Last Post</th>
          </tr>
        </thead>
        <tbody>
          {% for board in boards %}
            <tr>
              <td>
                {{ board.name }}
                <small class="text-muted d-block">{{ board.description }}</small>
              </td>
              <td class="align-middle">0</td>
              <td class="align-middle">0</td>
              <td></td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </body>
</html>
```

The result now:

![Boards Homepage Bootstrap](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-bootstrap-2.png)

So far we are adding new boards using the interactive console (`python manage.py shell`). But we need a better way to do it. In the next section, we are going to implement an admin interface for the website administrator manage it.

------

#### Introduction to Django Admin

When we start a new project, Django already comes configured with the **Django Admin** listed in the `INSTALLED_APPS`.

![Django Admin Comic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/Pixton_Comic_Django_Admin.png)

A good use case of the Django Admin is for example in a blog; it can be used by the authors to write and publish articles. Another example is an e-commerce website, where the staff members can create, edit, delete products.

For now, we are going to configure the Django Admin to maintain our application’s boards.

==Let’s start by creating an administrator account==:

```
python manage.py createsuperuser
```

Follow the instructions:

```
Username (leave blank to use 'vitorfs'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

Now open the URL in a web browser: **http://127.0.0.1:8000/admin/**

![Django Admin Login](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin-login.png)

Enter the **username** and **password** to log into the administration interface:

![Django Admin](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin.png)

It already comes with some features configured. Here we can add **Users** and **Groups** to manage permissions. We will explore more of those concepts later on.

==To add the **Board** model is very straightforward. Open the **admin.py** file in the **boards** directory, and add the following code==:

**boards/admin.py**

```python
from django.contrib import admin
from .models import Board

admin.site.register(Board)
```

Save the **admin.py** file, and refresh the page on your web browser:

![Django Admin Boards](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin-boards.png)

And that’s it! It’s ready to be used. Click on the **Boards** link to see the list of existing boards:

![Django Admin Boards List](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin-boards-list.png)

We can add a new board by clicking on the **Add Board** button:

![Django Admin Boards Add](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin-boards-add.png)

Click on the **save** button:

![Django Admin Boards List](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/django-admin-boards-list-2.png)

We can check if everything is working be opening the **http://127.0.0.1:8000** URL:

![Boards Homepage](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-2/boards-homepage-bootstrap-3.png)

------

#### Conclusions

In this tutorial, we explored many new concepts. We defined some requirements for our project, created the first models, migrated the database, started playing with the Models API. We created our very first view and wrote some unit tests. We also configured the Django Template Engine, Static Files, and added the Bootstrap 4 library to the project. Finally, we had a very brief introduction the Django Admin interface.

I hope you enjoyed the second part of this tutorial series! The third part is coming out next week, on Sep 18, 2017. In the next part, we are going to explore Django’s URL routing, the forms API, reusable templates, and more testing. If you would like to get notified when the third part is out, you can [subscribe to our mailing list](https://colossus.simpleisbetterthancomplex.com/subscribe/d2320a41-0378-4aa8-8f4e-5bb1ffcd521d/).

The source code of the project is available on GitHub. The current state of the project can be found under the release tag **v0.2-lw**. The link below will take you to the right place:

https://github.com/sibtc/django-beginners-guide/tree/v0.2-lw

------

[![A Complete Beginner's Guide to Django - Part 1](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-1/featured.jpg)← Part 1 - Getting Started](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)

[![A Complete Beginner's Guide to Django - Part 3](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/featured.jpg)Part 3 - Advanced Concepts →](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)

## Part 3 Advanced Concepts

#### Introduction

In this tutorial, we are going to dive deep into two fundamental concepts: URLs and Forms. In the process, we are going to explore many other concepts like creating reusable templates and installing third-party libraries. We are also going to write plenty of unit tests.

If you are following this tutorial series since the first part, coding your project and following the tutorial step by step, you may need to update your **models.py** before starting:

**boards/models.py**

```
class Topic(models.Model):
    # other fields...
    # Add `auto_now_add=True` to the `last_updated` field
    last_updated = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    # other fields...
    # Add `null=True` to the `updated_by` field
    updated_by = models.ForeignKey(User, null=True, related_name='+')
```

Now run the commands with the virtualenv activated:

```
python manage.py makemigrations
python manage.py migrate
```

If you already have `null=True` in the `updated_by` field and the `auto_now_add=True` in the `last_updated` field, you can safely ignore the instructions above.

If you prefer to use my source code as a starting point, you can grab it on GitHub.

The current state of the project can be found under the release tag **v0.2-lw**. The link below will take you to the right place:

https://github.com/sibtc/django-beginners-guide/tree/v0.2-lw

The development will follow from here.

------

#### URLs

Proceeding with the development of our application, now we have to implement a new page to list all the topics that belong to a given **Board**. Just to recap, below you can see the wireframe we drew in the previous tutorial:

![Wireframe Topics](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/wireframe-topics.png)

Figure 1: Boards project wireframe listing all topics in the Django board.

We will start by editing the **urls.py** inside the **myproject** folder:

**myproject/urls.py**

```python
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^admin/', admin.site.urls),
]
```

This time let’s take a moment and analyze the `urlpatterns` and `url`.

The URL dispatcher and **URLconf** (URL configuration) are fundamental parts of a Django application. In the beginning, it can look confusing; I remember having a hard time when I first started developing with Django.

In fact, right now the Django Developers are working on a [proposal to make simplified routing syntax](https://github.com/django/deps/blob/master/accepted/0201-simplified-routing-syntax.rst). But for now, as per the version 1.11, that’s what we have. So let’s try to understand how it works.

A project can have many **urls.py** distributed among the apps. But Django needs a **url.py** to use as a starting point. This special **urls.py** is called **root URLconf**. It’s defined in the **settings.py** file.

**myproject/settings.py**

```
ROOT_URLCONF = 'myproject.urls'
```

It already comes configured, so you don’t need to change anything here.

When Django receives a request, it starts searching for a match in the project’s URLconf. It starts with the first entry of the `urlpatterns` variable, and test the requested URL against each `url` entry.

==If Django finds a match, it will pass the request to the **view function**, which is the second parameter of the `url`.== The order in the `urlpatterns` matters, because Django will stop searching as soon as it finds a match. Now, if Django doesn’t find a match in the URLconf, it will raise a **404** exception, which is the error code for **Page Not Found**.

==This is the anatomy of the `url` function:==

```python
def url(regex, view, kwargs=None, name=None):
    # ...
```

- **regex**: A regular expression for matching URL patterns in strings. Note that these regular expressions do not search **GET** or **POST** parameters. In a request to **http://127.0.0.1:8000/boards/?page=2** only **/boards/** will be processed.
- **view**: A view function used to process the user request for a matched URL. It also accepts the return of the **django.conf.urls.include** function, which is used to reference an external **urls.py** file. You can, for example, use it to define a set of app specific URLs, and include it in the root URLconf using a prefix. We will explore more on this concept later on.
- **kwargs**: Arbitrary keyword arguments that’s passed to the target view. It is normally used to do some simple customization on reusable views. We don’t use it very often.
- **name**: A unique identifier for a given URL. This is a very important feature. Always remember to name your URLs. With this, you can change a specific URL in the whole project by just changing the regex. So it’s important to never hard code URLs in the views or templates, and always refer to the URLs by its name.

![Matching URL patterns](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/Pixton_Comic_URL_Patterns.png)

##### Basic URLs

Basic URLs are very simple to create. It’s just a matter of matching strings. For example, let’s say we wanted to create an “about” page, it could be defined like this:

```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
]
```

We can also create deeper URL structures:

```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about/company/$', views.about_company, name='about_company'),
    url(r'^about/author/$', views.about_author, name='about_author'),
    url(r'^about/author/vitor/$', views.about_vitor, name='about_vitor'),
    url(r'^about/author/erica/$', views.about_erica, name='about_erica'),
    url(r'^privacy/$', views.privacy_policy, name='privacy_policy'),
]
```

Those are some examples of simple URL routing. For all the examples above, the view function will follow this structure:

```python
def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})
```

##### Advanced URLs

A more advanced usage of URL routing is achieved by taking advantage of the regex to match certain types of data and create **dynamic** URLs.

For example, to create a profile page, like many services do like github.com/vitorfs or twitter.com/vitorfs, where “vitorfs” is my username, we can do the following:

```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
]
```

This will match all valid usernames for a Django User model.

Now observe that the example above is a very *permissive* URL. That means it will match lots of URL patterns because it is defined in the root of the URL, with no prefix like **/profile/<username>/**. In this case, if we wanted to define a URL named **/about/**, we would have do define it *before* the username URL pattern:

```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
]
```

If the “about” page was defined *after* the username URL pattern, Django would never find it, because the word “about” would match the username regex, and the view `user_profile` would be processed instead of the `about` view function.

There are some side effects to that. For example, from now on, we would have to treat “about” as a forbidden username, because if a user picked “about” as their username, this person would never see their profile page.

![URL routing order matters](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/Pixton_Comic_The_Order_Matters.png)

 **Sidenote:** If you want to design cool URLs for user profiles, the easiest solution to avoid URL collision is by adding a prefix like **/u/vitorfs/**, or like Medium does **/@vitorfs/**, where "@" is the prefix.

If you want no prefix at all, consider using a list of forbidden names like this: [github.com/shouldbee/reserved-usernames](https://github.com/shouldbee/reserved-usernames/blob/master/reserved-usernames.csv). Or another example is an application I developed when I was learning Django; I created my list at the time: [github.com/vitorfs/parsifal/](https://github.com/vitorfs/parsifal/blob/master/parsifal/authentication/forms.py#L6).

Those collisions are very common. Take GitHub for example; they have this URL to list all the repositories you are currently watching: [github.com/watching](https://github.com/watching). Someone registered a username on GitHub with the name "watching," so this person can't see his profile page. We can see a user with this username exists by trying this URL: [github.com/watching/repositories](https://github.com/watching/repositories) which was supposed to list the user's repositories, like mine for example [github.com/vitorfs/repositories](https://github.com/vitorfs/repositories).

==The whole idea of this kind of URL routing is to create dynamic pages where part of the URL will be used as an identifier for a certain resource, that will be used to compose a page==. This identifier can be an integer ID or a string for example.

Initially, we will be working with the **Board** ID to create a dynamic page for the **Topics**. Let’s read again the example I gave at the beginning of the **URLs** section:

```python
url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')
```

==The regex `\d+` will match an integer of arbitrary size.== This integer will be used to retrieve the **Board** from the database. Now observe that we wrote the regex as `(?P<pk>\d+)`, ==this is telling Django to capture the value into a keyword argument named **pk**==.

Here is how we write a view function for it:

```python
def board_topics(request, pk):
    # do something...
```

Because we used the `(?P<pk>\d+)` regex, the keyword argument in the `board_topics` must be named **pk**.

If we wanted to use any name, we could do it like this:

```python
url(r'^boards/(\d+)/$', views.board_topics, name='board_topics')
```

Then the view function could be defined like this:

```python
def board_topics(request, board_id):
    # do something...
```

Or like this:

```python
def board_topics(request, id):
    # do something...
```

The name wouldn’t matter. But it’s a good practice to use named parameters because when we start composing bigger URLs capturing multiple IDs and variables, it will be easier to read.

 **Sidenote:** PK or ID?

**PK** stands for **Primary Key**. It's a shortcut for accessing a model's primary key. All Django models have this attribute.

For the most cases, using the `pk` property is the same as `id`. That's because if we don't define a primary key for a model, Django will automatically create an `AutoField` named `id`, which will be its primary key.

If you defined a different primary key for a model, for example, let's say the field `email` is your primary key. To access it you could either use `obj.email` or `obj.pk`.

##### Using the URLs API

It’s time to write some code. Let’s implement the topic listing page (see [Figure 1](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#figure-1)) I mentioned at the beginning of the **URLs** section.

First, edit the **urls.py** adding our new URL route:

**myproject/urls.py**

```python
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^admin/', admin.site.urls),
]
```

Now let’s create the view function `board_topics`:

**boards/views.py**

```python
from django.shortcuts import render
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
```

In the **templates** folder, create a new template named **topics.html**:

**templates/topics.html**

```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item">Boards</li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>
```

 **Note:** For now we are simply creating new HTML templates. No worries, in the following section I will show you how to create reusable templates.

Now check the URL **http://127.0.0.1:8000/boards/1/** in a web browser. The result should be the following page:

![Topics Page](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-1.png)

Time to write some tests! Edit the **tests.py** file and add the following tests in the bottom of the file:

**boards/tests.py**

```python
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board

class HomeTests(TestCase):
    # ...

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
```

A few things to note here. This time we used the `setUp` method. In the setup method, we created a **Board** instance to use in the tests. We have to do that because the Django testing suite doesn’t run your tests against the current database. To run the tests Django creates a new database on the fly, applies all the model migrations, runs the tests, and when done, destroys the testing database.

So in the `setUp` method, we prepare the environment to run the tests, so to simulate a scenario.

- The `test_board_topics_view_success_status_code` method: is testing if Django is returning a status code 200 (success) for an existing **Board**.
- The `test_board_topics_view_not_found_status_code` method: is testing if Django is returning a status code 404 (page not found) for a **Board** that doesn’t exist in the database.
- The `test_board_topics_url_resolves_board_topics_view` method: is testing if Django is using the correct view function to render the topics.

Now it’s time to run the tests:

```
python manage.py test
```

And the output:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.E...
======================================================================
ERROR: test_board_topics_view_not_found_status_code (boards.tests.BoardTopicsTests)
----------------------------------------------------------------------
Traceback (most recent call last):
# ...
boards.models.DoesNotExist: Board matching query does not exist.

----------------------------------------------------------------------
Ran 5 tests in 0.093s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

The test **test_board_topics_view_not_found_status_code** failed. We can see in the Traceback it returned an exception “boards.models.DoesNotExist: Board matching query does not exist.”

![Topics Error 500 Page](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-error-500.png)

In production with `DEBUG=False`, the visitor would see a **500 Internal Server Error** page. But that’s not the behavior we want.

We want to show a **404 Page Not Found**. So let’s refactor our view:

**boards/views.py**

```
from django.shortcuts import render
from django.http import Http404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
```

Let’s test again:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.042s

OK
Destroying test database for alias 'default'...
```

Yay! Now it’s working as expected.

![Topics Error 404 Page](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-error-404.png)

This is the default page Django show while with `DEBUG=False`. Later on, we can customize the 404 page to show something else.

Now that’s a very common use case. In fact, Django has a shortcut to try to get an object, or return a 404 with the object does not exist.

So let’s refactor the **board_topics** view again:

```
from django.shortcuts import render, get_object_or_404
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
```

Changed the code? Test it.

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.052s

OK
Destroying test database for alias 'default'...
```

Didn’t break anything. We can proceed with the development.

The next step now is to create the navigation links in the screens. The homepage should have a link to take the visitor to the topics page of a given **Board**. Similarly, the topics page should have a link back to the homepage.

![Wireframe Links](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/wireframe-links.png)

We can start by writing some tests for the `HomeTests` class:

**boards/tests.py**

```
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
```

Observe that now we added a **setUp** method for the **HomeTests** as well. That’s because now we are going to need a **Board** instance and also we moved the **url** and **response** to the **setUp**, so we can reuse the same response in the new test.

The new test here is the **test_home_view_contains_link_to_topics_page**. Here we are using the **assertContains** method to test if the response body contains a given text. The text we are using in the test, is the `href` part of an `a` tag. So basically we are testing if the response body has the text `href="/boards/1/"`.

Let’s run the tests:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....F.
======================================================================
FAIL: test_home_view_contains_link_to_topics_page (boards.tests.HomeTests)
----------------------------------------------------------------------
# ...

AssertionError: False is not true : Couldn't find 'href="/boards/1/"' in response

----------------------------------------------------------------------
Ran 6 tests in 0.034s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

Now we can write the code that will make this test pass.

Edit the **home.html** template:

**templates/home.html**

```
<!-- code suppressed for brevity -->
<tbody>
  {% for board in boards %}
    <tr>
      <td>
        <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
        <small class="text-muted d-block">{{ board.description }}</small>
      </td>
      <td class="align-middle">0</td>
      <td class="align-middle">0</td>
      <td></td>
    </tr>
  {% endfor %}
</tbody>
<!-- code suppressed for brevity -->
```

So basically we changed the line:

```
{{ board.name }}
```

To:

```
<a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
```

Always use the `{% url %}` template tag to compose the applications URLs. The first parameter is the **name** of the URL (defined in the URLconf, i.e., the **urls.py**), then you can pass an arbitrary number of arguments as needed.

If it were a simple URL, like the homepage, it would be just `{% url 'home' %}`.

Save the file and run the tests again:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.037s

OK
Destroying test database for alias 'default'...
```

Good! Now we can check how it looks in the web browser:

![Boards with Link](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/boards.png)

Now the link back. We can write the test first:

**boards/tests.py**

```
class BoardTopicsTests(TestCase):
    # code suppressed for brevity...

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
```

Run the tests:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.F.....
======================================================================
FAIL: test_board_topics_view_contains_link_back_to_homepage (boards.tests.BoardTopicsTests)
----------------------------------------------------------------------
Traceback (most recent call last):
# ...

AssertionError: False is not true : Couldn't find 'href="/"' in response

----------------------------------------------------------------------
Ran 7 tests in 0.054s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

Update the board topics template:

**templates/topics.html**

```
{% load static %}<!DOCTYPE html>
<html>
  <head><!-- code suppressed for brevity --></head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>
```

Run the tests:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.061s

OK
Destroying test database for alias 'default'...
```

![Board Topics with Link](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/board_topics.png)

As I mentioned before, URL routing is a fundamental part of a web application. With this knowledge, we should be able to proceed with the development. Next, to complete the section about URLs, you will find a summary of useful URL patterns.

##### List of Useful URL Patterns

The trick part is the **regex**. So I prepared a list of the most used URL patterns. You can always refer to this list when you need a specific URL.

| Primary Key AutoField |                                                              |
| :-------------------- | ------------------------------------------------------------ |
| Regex                 | `(?P<pk>\d+)`                                                |
| Example               | `url(r'^questions/(?P<pk>\d+)/$', views.question, name='question')` |
| Valid URL             | `/questions/934/`                                            |
| Captures              | `{'pk': '934'}`                                              |

| Slug Field |                                                              |
| :--------- | ------------------------------------------------------------ |
| Regex      | `(?P<slug>[-\w]+)`                                           |
| Example    | `url(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post')` |
| Valid URL  | `/posts/hello-world/`                                        |
| Captures   | `{'slug': 'hello-world'}`                                    |

| Slug Field with Primary Key |                                                              |
| :-------------------------- | ------------------------------------------------------------ |
| Regex                       | `(?P<slug>[-\w]+)-(?P<pk>\d+)`                               |
| Example                     | `url(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post')` |
| Valid URL                   | `/blog/hello-world-159/`                                     |
| Captures                    | `{'slug': 'hello-world', 'pk': '159'}`                       |

| Django User Username |                                                              |
| :------------------- | ------------------------------------------------------------ |
| Regex                | `(?P<username>[\w.@+-]+)`                                    |
| Example              | `url(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile')` |
| Valid URL            | `/profile/vitorfs/`                                          |
| Captures             | `{'username': 'vitorfs'}`                                    |

| Year      |                                                              |
| :-------- | ------------------------------------------------------------ |
| Regex     | `(?P<year>[0-9]{4})`                                         |
| Example   | `url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year')` |
| Valid URL | `/articles/2016/`                                            |
| Captures  | `{'year': '2016'}`                                           |

| Year / Month |                                                              |
| :----------- | ------------------------------------------------------------ |
| Regex        | `(?P<year>[0-9]{4})/(?P<month>[0-9]{2})`                     |
| Example      | `url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month')` |
| Valid URL    | `/articles/2016/01/`                                         |
| Captures     | `{'year': '2016', 'month': '01'}`                            |

You can find more details about those patterns in this post: [List of Useful URL Patterns](https://simpleisbetterthancomplex.com/references/2016/10/10/url-patterns.html).

------

#### Reusable Templates

Until now we’ve been copying and pasting HTML repeating several parts of the HTML document, which is not very sustainable in the long run. It’s also a bad practice.

In this section we are going to refactor our HTML templates, creating a **master page** and only adding the unique part for each template.

Create a new file named **base.html** in the **templates** folder:

**templates/base.html**

```
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```

This is going to be our master page. Every template we create, is going to **extend** this special template. Observe now we introduced the `{% block %}` tag. It is used to reserve a space in the template, which a “child” template (which extends the master page) can insert code and HTML within that space.

In the case of the `{% block title %}` we are also setting a default value, which is “Django Boards.” It will be used if we don’t set a value for the `{% block title %}` in a child template.

Now let’s refactor our two templates: **home.html** and **topics.html**.

**templates/home.html**

```
{% extends 'base.html' %}

{% block breadcrumb %}
  <li class="breadcrumb-item active">Boards</li>
{% endblock %}

{% block content %}
  <table class="table">
    <thead class="thead-inverse">
      <tr>
        <th>Board</th>
        <th>Posts</th>
        <th>Topics</th>
        <th>Last Post</th>
      </tr>
    </thead>
    <tbody>
      {% for board in boards %}
        <tr>
          <td>
            <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
            <small class="text-muted d-block">{{ board.description }}</small>
          </td>
          <td class="align-middle">0</td>
          <td class="align-middle">0</td>
          <td></td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

The first line in the **home.html** template is `{% extends 'base.html' %}`. This tag is telling Django to use the **base.html** template as a master page. After that, we are using the the *blocks* to put the unique content of the page.

**templates/topics.html**

```
{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
    <!-- just leaving it empty for now. we will add core here soon. -->
{% endblock %}
```

In the **topics.html** template, we are changing the `{% block title %}` default value. Notice that we can reuse the default value of the block by calling `{{ block.super }}`. So here we are playing with the website title, which we defined in the **base.html** as “Django Boards.” So for the “Python” board page, the title will be “Python - Django Boards,” for the “Random” board the title will be “Random - Django Boards.”

Now let’s run the tests and see we didn’t break anything:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.067s

OK
Destroying test database for alias 'default'...
```

Great! Everything is looking good.

Now that we have the **base.html** template, we can easily add a top bar with a menu:

**templates/base.html**

```
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
      </div>
    </nav>

    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```

![Django Boards Header](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/django-boards-header-1.png)

![Django Boards Header](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/django-boards-header-2.png)

The HTML I used is part of the [Bootstrap 4 Navbar Component](https://getbootstrap.com/docs/4.0/components/navbar/).

A nice touch I like to add is to change the font in the “logo” (`.navbar-brand`) of the page.

Go to [fonts.google.com](https://fonts.google.com/), type “Django Boards” or whatever name you gave to your project then click on **apply to all fonts**. Browse a bit, find one that you like.

![Google Fonts](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/google-fonts.png)

Add the font in the **base.html** template:

```
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
  </head>
  <body>
    <!-- code suppressed for brevity -->
  </body>
</html>
```

Now create a new CSS file named **app.css** inside the **static/css** folder:

**static/css/app.css**

```
.navbar-brand {
  font-family: 'Peralta', cursive;
}
```

![Django Boards Logo](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/boards-logo.png)

------

#### Forms

Forms are used to deal with user input. It’s a very common task in any web application or website. The standard way to do it is through HTML forms, where the user input some data, submit it to the server, and then the server does something with it.

![All input is evil](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/Pixton_Comic_All_Input.png)

Form processing is a fairly complex task because it involves interacting with many layers of an application. There are also many issues to take care of. For example, all data submitted to the server comes in a string format, so we have to transform it into a proper data type (integer, float, date, etc.) before doing anything with it. We have to validate the data regarding the business logic of the application. We also have to clean, sanitize the data properly so to avoid security issues such as SQL Injection and XSS attacks.

Good news is that the Django Forms API makes the whole process a lot easier, automating a good chunk of this work. Also, the final result is a much more secure code than most programmers would be able to implement by themselves. So, no matter how simple the HTML form is, always use the forms API.

##### How Not Implement a Form

At first, I thought about jumping straight to the forms API. But I think it would be a good idea for us to spend some time trying to understand the underlying details of form processing. Otherwise, it will end up looking like magic, which is a bad thing, because when things go wrong, you have no idea where to look for the problem.

With a deeper understanding of some programming concepts, we can feel more in control of the situation. Being in control is important because it let us write code with more confidence. The moment we know exactly what is going on, it’s much easier to implement a code of predictable behavior. It’s also a lot easier to debug and find errors because you know where to look.

Anyway, let’s start by implementing the form below:

![Wireframe New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/wireframe-new-topic.png)

It’s one of the wireframes we drew in the previous tutorial. I now realize this may be a bad example to start because this particular form involves processing data of two different models: **Topic** (subject) and **Post** (message).

There’s another important aspect that we haven’t discussed it so far, which is user authentication. We are only supposed to show this screen for authenticated users. This way we can tell who created a **Topic** or a **Post**.

So let’s abstract some details for now and focus on understanding how to save user input in the database.

First thing, let’s create a new URL route named **new_topic**:

**myproject/urls.py**

```
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
```

The way we are building the URL will help us identify the correct **Board**.

Now let’s create the **new_topic** view function:

**boards/views.py**

```
from django.shortcuts import render, get_object_or_404
from .models import Board

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
```

For now, the **new_topic** view function is looking exactly the same as the **board_topics**. That’s on purpose, let’s take a step at a time.

Now we just need a template named **new_topic.html** to see some code working:

**templates/new_topic.html**

```
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}

{% endblock %}
```

For now we just have the breadcrumb assuring the navigation. Observe that we included the URL back to the **board_topics** view.

Open the URL **http://127.0.0.1:8000/boards/1/new/**. The result, for now, is the following page:

![Start a New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/start-a-new-topic.png)

We still haven’t implemented a way to reach this new page, but if we change the URL to **http://127.0.0.1:8000/boards/2/new/**, it should take us to the **Python Board**:

![Start a New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/start-a-new-topic-python.png)

 **Note:**

The result may be different for you if you haven't followed the steps from the previous tutorial. In my case, I have three **Board** instances in the database, being Django = 1, Python = 2, and Random = 3. Those numbers are the IDs from the database, used from the URL to identify the right resource.

We can already add some tests:

**boards/tests.py**

```
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, board_topics, new_topic
from .models import Board

class HomeTests(TestCase):
    # ...

class BoardTopicsTests(TestCase):
    # ...

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))
```

A quick summary of the tests of our new class **NewTopicTests**:

- **setUp**: creates a **Board** instance to be used during the tests
- **test_new_topic_view_success_status_code**: check if the request to the view is successful
- **test_new_topic_view_not_found_status_code**: check if the view is raising a 404 error when the **Board** does not exist
- **test_new_topic_url_resolves_new_topic_view**: check if the right view is being used
- **test_new_topic_view_contains_link_back_to_board_topics_view**: ensure the navigation back to the list of topics

Run the tests:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 0.076s

OK
Destroying test database for alias 'default'...
```

Good, now it’s time to start creating the form.

**templates/new_topic.html**

```
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    <div class="form-group">
      <label for="id_subject">Subject</label>
      <input type="text" class="form-control" id="id_subject" name="subject">
    </div>
    <div class="form-group">
      <label for="id_message">Message</label>
      <textarea class="form-control" id="id_message" name="message" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

This is a raw HTML form created by hand using the CSS classes provided by Bootstrap 4. It looks like this:

![Start a New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/start-a-new-topic-form.png)

In the `<form>` tag, we have to define the `method` attribute. This instructs the browser on how we want to communicate with the server. The HTTP spec defines several request methods (verbs). But for the most part, we will only be using **GET** and **POST** request types.

**GET** is perhaps the most common request type. It’s used to *retrieve* data from the server. Every time you click on a link or type a URL directly into the browser, you are creating a **GET** request.

**POST** is used when we want to change data on the server. So, generally speaking, every time we send data to the server that will result in a change in the state of a resource, we should always send it via **POST** request.

Django protects all **POST** requests using a **CSRF Token** (Cross-Site Request Forgery Token). It’s a security measure to avoid external sites or applications to submit data to our application. Every time the application receives a **POST**, it will first look for the **CSRF Token**. If the request has no token, or the token is invalid, it will discard the posted data.

The result of the **csrf_token** template tag:

```
{% csrf_token %}
```

Is a hidden field that’s submitted along with the other form data:

```
<input type="hidden" name="csrfmiddlewaretoken" value="jG2o6aWj65YGaqzCpl0TYTg5jn6SctjzRZ9KmluifVx0IVaxlwh97YarZKs54Y32">
```

Another thing, we have to set the **name** of the HTML inputs. The **name** will be used to retrieve the data on the server side.

```
<input type="text" class="form-control" id="id_subject" name="subject">
<textarea class="form-control" id="id_message" name="message" rows="5"></textarea>
```

Here is how we retrieve the data:

```
subject = request.POST['subject']
message = request.POST['message']
```

So, a naïve implementation of a view that grabs the data from the HTML and starts a new topic can be written like this:

```
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
```

This view is only considering the *happy path*, which is receiving the data and saving it into the database. But there are some missing parts. We are not validating the data. The user could submit an empty form or a **subject** that’s bigger than 255 characters.

So far we are hard-coding the **User** fields because we haven’t implemented the authentication yet. But there’s an easy way to identify the logged in user. We will get to that part in the next tutorial. Also, we haven’t implemented the view where we will list all the posts within a topic, so upon success, we are redirecting the user to the page where we list all the board topics.

![Start a New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/start-a-new-topic-form-submit.png)

Submitted the form clicking on the **Post** button:

![Topics](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-2.png)

It looks like it worked. But we haven’t implemented the topics listing yet, so there’s nothing to see here. Let’s edit the **templates/topics.html** file to do a proper listing:

**templates/topics.html**

```
{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
  <table class="table">
    <thead class="thead-inverse">
      <tr>
        <th>Topic</th>
        <th>Starter</th>
        <th>Replies</th>
        <th>Views</th>
        <th>Last Update</th>
      </tr>
    </thead>
    <tbody>
      {% for topic in board.topics.all %}
        <tr>
          <td>{{ topic.subject }}</td>
          <td>{{ topic.starter.username }}</td>
          <td>0</td>
          <td>0</td>
          <td>{{ topic.last_updated }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

![Topics](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-3.png)

Yep! The **Topic** we created is here.

Two new concepts here:

We are using for the first time the **topics** property in the **Board** model. The **topics** property is created automatically by Django using a reverse relationship. In the previous steps, we created a **Topic** instance:

```
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    # ...

    topic = Topic.objects.create(
        subject=subject,
        board=board,
        starter=user
    )
```

In the line `board=board`, we set the **board** field in **Topic** model, which is a `ForeignKey(Board)`. With that, now our **Board** instance is aware that it has an **Topic** instance associated with it.

The reason why we used `board.topics.all` instead of just `board.topics` is because `board.topics` is a **Related Manager**, which is pretty much similar to a **Model Manager**, usually available on the `board.objects` property. So, to return all topics associated with a given board, we have to run `board.topics.all()`. To filter some data, we could do `board.topics.filter(subject__contains='Hello')`.

Another important thing to note is that, inside Python code, we have to use parenthesis: `board.topics.all()`, because `all()` is a method. When writing code using the Django Template Language, in an HTML template file, we don’t use parenthesis, so it’s just `board.topics.all`.

The second thing is that we are making use of a `ForeignKey`:

```
{{ topic.starter.username }}
```

Just create a *path* through the property using dots. We can pretty much access any property of the **User** model. If we wanted the user’s email, we could use `topic.starter.email`.

Since we are already modifying the **topics.html** template, let’s create the button that takes us to the **new topic** screen:

**templates/topics.html**

```
{% block content %}
  <div class="mb-4">
    <a href="{% url 'new_topic' board.pk %}" class="btn btn-primary">New topic</a>
  </div>

  <table class="table">
    <!-- code suppressed for brevity -->
  </table>
{% endblock %}
```

![Topics](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/topics-4.png)

We can include a test to make sure the user can reach the **New topic** view from this page:

**boards/tests.py**

```
class BoardTopicsTests(TestCase):
    # ...

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
```

Basically here I renamed the old **test_board_topics_view_contains_link_back_to_homepage** method and add an extra `assertContains`. This test is now responsible for making sure our view contains the required navigation links.

##### Testing The Form View

Before we code the previous form example in a Django way, let’s write some tests for the form processing:

**boards/tests.py**

```
''' new imports below '''
from django.contrib.auth.models import User
from .views import new_topic
from .models import Board, Topic, Post

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')  # <- included this line here

    # ...

    def test_csrf(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
```

First thing, the **tests.py** file is already starting to get big. We will improve it soon, breaking the tests into several files. But for now, let’s keep working on it.

- **setUp**: included the `User.objects.create_user` to create a **User** instance to be used in the tests
- **test_csrf**: since the **CSRF Token** is a fundamental part of processing **POST** requests, we have to make sure our HTML contains the token.
- **test_new_topic_valid_post_data**: sends a valid combination of data and check if the view created a **Topic** instance and a **Post** instance.
- **test_new_topic_invalid_post_data**: here we are sending an empty dictionary to check how the application is behaving.
- **test_new_topic_invalid_post_data_empty_fields**: similar to the previous test, but this time we are sending some data. The application is expected to validate and reject empty subject and message.

Let’s run the tests:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........EF.....
======================================================================
ERROR: test_new_topic_invalid_post_data (boards.tests.NewTopicTests)
----------------------------------------------------------------------
Traceback (most recent call last):
...
django.utils.datastructures.MultiValueDictKeyError: "'subject'"

======================================================================
FAIL: test_new_topic_invalid_post_data_empty_fields (boards.tests.NewTopicTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/vitorfs/Development/myproject/django-beginners-guide/boards/tests.py", line 115, in test_new_topic_invalid_post_data_empty_fields
    self.assertEquals(response.status_code, 200)
AssertionError: 302 != 200

----------------------------------------------------------------------
Ran 15 tests in 0.512s

FAILED (failures=1, errors=1)
Destroying test database for alias 'default'...
```

We have one failing test and one error. Both related to invalid user input. Instead of trying to fix it with the current implementation, let’s make those tests pass using the Django Forms API.

#### Creating Forms The Right Way

So, we came a long way since we started working with Forms. Finally, it’s time to use the Forms API.

The Forms API is available in the module `django.forms`. Django works with two types of forms: `forms.Form` and `forms.ModelForm`. The `Form` class is a general purpose form implementation. We can use it to process data that are not directly associated with a model in our application. A `ModelForm` is a subclass of `Form`, and it’s associated with a model class.

Let’s create a new file named **forms.py** inside the **boards**’ folder:

**boards/forms.py**

```
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']
```

This is our first form. It’s a `ModelForm` associated with the **Topic** model. The `subject` in the `fields` list inside the **Meta** class is referring to the `subject` field in the **Topic** class. Now observe that we are defining an extra field named `message`. This refers to the message in the **Post** we want to save.

Now we have to refactor our **views.py**:

**boards/views.py**

```
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
```

This is how we use the forms in a view. Let me remove the extra noise so we can focus on the core of the form processing:

```
if request.method == 'POST':
    form = NewTopicForm(request.POST)
    if form.is_valid():
        topic = form.save()
        return redirect('board_topics', pk=board.pk)
else:
    form = NewTopicForm()
return render(request, 'new_topic.html', {'form': form})
```

First we check if the request is a **POST** or a **GET**. If the request came from a **POST**, it means the user is submitting some data to the server. So we instantiate a form instance passing the **POST** data to the form: `form = NewTopicForm(request.POST)`.

Then, we ask Django to verify the data, check if the form is valid if we can save it in the database: `if form.is_valid():`. If the form was valid, we proceed to save the data in the database using `form.save()`. The `save()` method returns an instance of the Model saved into the database. So, since this is a **Topic** form, it will return the **Topic** that was created: `topic = form.save()`. After that, the common path is to redirect the user somewhere else, both to avoid the user re-submitting the form by pressing F5 and also to keep the flow of the application.

Now, if the data was invalid, Django will add a list of errors to the form. After that, the view does nothing and returns in the last statement: `return render(request, 'new_topic.html', {'form': form})`. That means we have to update the **new_topic.html** to display errors properly.

If the request was a **GET**, we just initialize a new and empty form using `form = NewTopicForm()`.

Let’s run the tests and see how is everything:

```
python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...............
----------------------------------------------------------------------
Ran 15 tests in 0.522s

OK
Destroying test database for alias 'default'...
```

We even fixed the last two tests.

The Django Forms API does much more than processing and validating the data. It also generates the HTML for us.

Let’s update the **new_topic.html** template to fully use the Django Forms API:

**templates/new_topic.html**

```
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

The `form` have three rendering options: `form.as_table`, `form.as_ul`, and `form.as_p`. It’s a quick way to render all the fields of a form. As the name suggests, the `as_table` uses table tags to format the inputs, the `as_ul` creates an HTML list of inputs, etc.

Let’s see how it looks like:

![Start a New Topic](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/start-a-new-topic-form-django.png)

Well, our previous form was looking better, right? We are going to fix it in a moment.

It can look broken right now but trust me; there’s a lot of things behind it right now. And it’s extremely powerful. For example, if our form had 50 fields, we could render all the fields just by typing `{{ form.as_p }}`.

And more, using the Forms API, Django will validate the data and add error messages to each field. Let’s try submitting an empty form:

![Form Validation](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/form-validation.png)

 **Note:**

If you see something like this: ![Please fill out this field.](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/novalidate.png) when you submit the form, that's not Django. It's your browser doing a pre-validation. To disable it add the `novalidate` attribute to your form tag: `<form method="post" novalidate>`

You can keep it; there's no problem with it. It's just because our form is very simple right now, and we don't have much data validation to see.

Another important thing to note is that: there is no such a thing as "client-side validation." JavaScript validation or browser validation is just for **usability** purpose. And also to reduce the number of requests to the server. Data validation should always be done on the server side, where we have full control over the data.

It also handles help texts, which can be defined both in a **Form** class or in a **Model** class:

**boards/forms.py**

```
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
```

![Help Text](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/help-text.png)

We can also set extra attributes to a form field:

**boards/forms.py**

```
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
```

![Form Placeholder](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/form-placeholder.png)

##### Rendering Bootstrap Forms

Alright, so let’s make things pretty again.

When working with Bootstrap or any other Front-End library, I like to use a Django package called **django-widget-tweaks**. It gives us more control over the rendering process, keeping the defaults and just adding extra customizations on top of it.

Let’s start off by installing it:

```
pip install django-widget-tweaks
```

Now add it to the `INSTALLED_APPS`:

**myproject/settings.py**

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'boards',
]
```

Now let’s take it into use:

**templates/new_topic.html**

```
{% extends 'base.html' %}

{% load widget_tweaks %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post" novalidate>
    {% csrf_token %}

    {% for field in form %}
      <div class="form-group">
        {{ field.label_tag }}

        {% render_field field class="form-control" %}

        {% if field.help_text %}
          <small class="form-text text-muted">
            {{ field.help_text }}
          </small>
        {% endif %}
      </div>
    {% endfor %}

    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

![Bootstrap Form](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/bootstrap-form.png)

There it is! So, here we are using the **django-widget-tweaks**. First, we load it in the template by using the `{% load widget_tweaks %}` template tag. Then the usage:

```
{% render_field field class="form-control" %}
```

The `render_field` tag is not part of Django; it lives inside the package we installed. To use it we have to pass a form field instance as the first parameter, and then after we can add arbitrary HTML attributes to complement it. It will be useful because then we can assign classes based on certain conditions.

Some examples of the `render_field` template tag:

```
{% render_field form.subject class="form-control" %}
{% render_field form.message class="form-control" placeholder=form.message.label %}
{% render_field field class="form-control" placeholder="Write a message!" %}
{% render_field field style="font-size: 20px" %}
```

Now to implement the Bootstrap 4 validation tags, we can change the **new_topic.html** template:

**templates/new_topic.html**

```
<form method="post" novalidate>
  {% csrf_token %}

  {% for field in form %}
    <div class="form-group">
      {{ field.label_tag }}

      {% if form.is_bound %}
        {% if field.errors %}

          {% render_field field class="form-control is-invalid" %}
          {% for error in field.errors %}
            <div class="invalid-feedback">
              {{ error }}
            </div>
          {% endfor %}

        {% else %}
          {% render_field field class="form-control is-valid" %}
        {% endif %}
      {% else %}
        {% render_field field class="form-control" %}
      {% endif %}

      {% if field.help_text %}
        <small class="form-text text-muted">
          {{ field.help_text }}
        </small>
      {% endif %}
    </div>
  {% endfor %}

  <button type="submit" class="btn btn-success">Post</button>
</form>
```

The result is this:

![Bootstrap Form Invalid](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/bootstrap-invalid-1.png)

![Bootstrap Form Partially Valid](https://simpleisbetterthancomplex.com/media/series/beginners-guide/1.11/part-3/bootstrap-invalid-2.png)

So, we have three different rendering states:

- **Initial state**: the form has no data (is not bound)
- **Invalid**: we add the `.is-invalid` CSS class and add error messages in an element with a class `.invalid-feedback`. The form field and the messages are rendered in red.
- **Valid**: we add the `.is-valid` CSS class so to paint the form field in green, giving feedback to the user that this field is good to go.

##### Reusable Forms Templates

The template code looks a little bit complicated, right? Well, the good news is that we can reuse this snippet across the project.

In the **templates** folder, create a new folder named **includes**:

```
myproject/
 |-- myproject/
 |    |-- boards/
 |    |-- myproject/
 |    |-- templates/
 |    |    |-- includes/    <-- here!
 |    |    |-- base.html
 |    |    |-- home.html
 |    |    |-- new_topic.html
 |    |    +-- topics.html
 |    +-- manage.py
 +-- venv/
```

Now inside the **includes** folder, create a file named **form.html**:

**templates/includes/form.html**

```
{% load widget_tweaks %}

{% for field in form %}
  <div class="form-group">
    {{ field.label_tag }}

    {% if form.is_bound %}
      {% if field.errors %}
        {% render_field field class="form-control is-invalid" %}
        {% for error in field.errors %}
          <div class="invalid-feedback">
            {{ error }}
          </div>
        {% endfor %}
      {% else %}
        {% render_field field class="form-control is-valid" %}
      {% endif %}
    {% else %}
      {% render_field field class="form-control" %}
    {% endif %}

    {% if field.help_text %}
      <small class="form-text text-muted">
        {{ field.help_text }}
      </small>
    {% endif %}
  </div>
{% endfor %}
```

Now we change our **new_topic.html** template:

**templates/new_topic.html**

```
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post" novalidate>
    {% csrf_token %}
    {% include 'includes/form.html' %}
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

As the name suggests, the `{% include %}` is used to *include* HTML templates in another template. It’s a very useful way to reuse HTML components in a project.

The next form we implement, we can simply use `{% include 'includes/form.html' %}` to render it.

##### Adding More Tests

Now we are using Django Forms; we can add more tests to make sure it is running smoothly:

**boards/tests.py**

```
# ... other imports
from .forms import NewTopicForm

class NewTopicTests(TestCase):
    # ... other tests

    def test_contains_form(self):  # <- new test
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):  # <- updated this one
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
```

Now we are using the `assertIsInstance` method for the first time. Basically we are grabbing the form instance in the context data, and checking if it is a `NewTopicForm`. In the last test, we added the `self.assertTrue(form.errors)` to make sure the form is showing errors when the data is invalid.

------

#### Conclusions

In this tutorial, we focused on URLs, Reusable Templates, and Forms. As usual, we also implement several test cases. That’s how we develop with confidence.

Our tests file is starting to get big, so in the next tutorial, we are going to refactor it to improve the maintainability so to sustain the growth of our code base.

We are also reaching a point where we need to interact with the logged in user. In the next tutorial, we are going to learn everything about authentication and how to protect our views and resources.

I hope you enjoyed the third part of this tutorial series! The fourth part is coming out next week, on Sep 25, 2017. If you would like to get notified when the fourth part is out, you can [subscribe to our mailing list](https://colossus.simpleisbetterthancomplex.com/subscribe/d2320a41-0378-4aa8-8f4e-5bb1ffcd521d/).

The source code of the project is available on GitHub. The current state of the project can be found under the release tag **v0.3-lw**. The link below will take you to the right place:

https://github.com/sibtc/django-beginners-guide/tree/v0.3-lw
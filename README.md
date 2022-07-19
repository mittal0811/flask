---
title: Flask
description: A popular minimal server framework for Python.
tags:
  - python
  - flask
---

# Python Flask Example

This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that serves a simple JSON response.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new?template=https%3A%2F%2Fgithub.com%2Frailwayapp%2Fexamples%2Ftree%2Fmaster%2Fexamples%2Fflask)

## ✨ Features

- Python
- Flask

## 💁‍♀️ How to use

- create a pipenv environment using "pipenv shell" in the main.py folder
- run "pipenv install" <-- this will install the require dependency listed in pipfile>
- use flask run command to start ( make sure FLASK_ENV is set to "main" using export in linux or mac)

# Here is what I learned while installing this project:

- I tried pipenv and installed all depenedencies in addition to gunicorn,
  and it works perfectly with Heroku buildpack mentioned in railway.app flask
  implementation, it works for sure for this project.

- mysqlclient does not seem to work on regular implmentation given by railway.app

- mysqlclient does not also working on local machine in pipenv as it does not have
  access to the mysqlclient of local machine. To make it work on local machine:
  use pip instead of pipenv for local machine.

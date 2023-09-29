# Loans App - Django

## About


## Setting Up Locally For Development

Table Of Contents

- [Setting Up Locally For Development](#setting-up-locally-for-development)
  - [Requirements](#requirements)
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)
  - [Step 5](#step-5)
  - [Step 6](#step-6)
  - [Step 7](#step-7)

## Requirements

**Python.**

*Windows Installation.*

**1. To run a Python or Django project, you first of all need to download and install Python. The Python download requires about 30MB of disk space. Follow this link [here](https://www.python.org/downloads/) to download Python.**

**2. Underneath the heading at the top that says `Python Releases for Windows`, click on the link for the `Latest Python 3 Release - Python 3.x.x`.**

**3. Scroll to the bottom and select either `Windows x64 executable installer` for 64-bit or `Windows x86 executable installer` for 32-bit.**

**4. Once you have chosen and downloaded an installer, simply run it by double-clicking on the `downloaded file`.**

>**Important:** You want to be sure to check the box that says **Add Python 3.x to PATH** as shown to ensure that the interpreter will be placed in your execution path.

**5. Then just click `Install Now`. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.**

*Linux/MacOS Installation.*

**1. There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.**

>To find out what version(s) you have, open a terminal window and try the following commands:

```sh
python --version
python2 --version
python3 --version
```

>One or more of these commands should respond with a version, as below:

```sh
python3 --version
Python 3.8.10
```

---

**Whenever you are starting a new Django project, it's a good idea to first set up your development environment. Create a new directory for your project to live in, and navigate into it. In shell:**

## Step 1

Clone the project and navigate into the main project folder

```sh
git clone https://github.com/CalebAckom/Loans_App.git
cd Loans_App
```

---

## Step 2

Create A Virtual Environment

A [virtual environment](https://docs.python.org/3/tutorial/venv.html) is recommended. See the [setup information](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).**

Ubuntu / MacOS

```sh
python3 -m venv venv
source venv/bin/activate
```

 >**Note:** If you don't use a virtual environment on Ubuntu or MacOS, you will need to specify your python or pip version at every of the following steps

Windows

```sh
pip install virtualenv
source \venv\Scripts\activate.bat
```

---

## Step 3

Update pip
>For Windows

```sh
pip install --upgrade pip
```

>For MacOS/Ubuntu

```sh
pip install --upgrade pip
```

## Step 4

Install all the Requirements. The `requirements.txt` file contains all packages needed to run this project. Instead of running the individual commands one after the other, Python provides a very easy way of getting all packages installed without stress. Just a line of code and we are good!**

```sh
pip install -r requirements.txt
```

>After this step all packages required for the project are installed. Among them especially Django, Django RestFramework, Django Corsheaders and dotenv.

---

## Step 5

This Project is using a .env file for API-Keys and some individual configurations. The command below makes a copy of the `.env.example` and names it `.env`. This environment file contains very sensitive information and must not be altered unless absolutely necessary.

```sh
cp .env.example .env
```

>You can simply generate the SECRET_KEY by using some [webservices](https://djecrety.ir).
---

## Step 6

Create and Migrate the Database.**

>This creates a database for the project where all current and future data are stored.

```sh
python3 manage makemigrations
python3 manage.py migrate
```

---

## Step 7

To get the project running, the server needs to be started. Use the command below to start the Server:

```sh
python3 manage.py runserver
```

**Congratulations. If you do not get an error, everything works fine, and you are done with the server side setup.**
**Go ahead and create a new branch and start developing**

**Happy Coding!**
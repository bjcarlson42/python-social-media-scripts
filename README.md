# Python Social Media Bot Collection

Marketing on social media is a monotonous task. Why spend time liking, commenting, tweeting, following, and unfollowing when you can write code to do it for you? That's exactly what I did. This repo is a collection of Python scripts that automate marketing on social media.

## Getting Started

Follow these instructions to get this project up and running on your machine and doing your social media marketing fast in no time!

### Prerequisites

You need the following installed on your machine for the project to work. If you have set up coding environments on your machine before you most likely can skip the following steps.

**Python**

- Navigate to https://www.python.org/downloads/ and download the latest version.

**Virtualenv**

```cmd
pip install virtualenv
```

**WebDriver for Chrome**

- Navigate to https://chromedriver.chromium.org/downloads and under **Current Releases** download the version for your Chrome Browser (81, 80, or 79).

- Unzip the file
- Run the following command

```cmd
mv ~Downloads/chromedriver /usr/local/bin
```

We are now able to clone the project and run it but before we do that, we will do a quick test to make sure everything works as expected. 

```cmd
mkdir <projectName>
virtualenv -p python3 <venvName>
source <venvName>/bin/activate
pip install selenium
cd <projectName>
touch test.py
```

In test.py:

```python
from selenium import webdriver

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://google.com)

Bot()
```

To run to above code:

```cmd
python -i main.py
```

If the above code opens chrome you have everything working correctly.

You can keep working in this or you can clone my repository. To do this, delete what you have just done be sure to use a different folder name in the next step. Run the following:

```cmd
mkdir <projectName>
virtualenv -p python3 venv
source venv/bin/activate
git clone <repo> . (be sure to include the dot)
pip install selenium
```

### Running the program

Before you run the porgram, you need to be aware of the two ways to give the program your password. The first is to make a secrets.py file and declare your password in there as a string, import that variable into the main program, and pass it in as a parameter. The other way (this is out of the box) is to enter your password each time you run the program. This is fine but the whole point of automation is to do the least amount of work. Entering your passwrod every time is just an extra step. If you want to create a secrets.py file, follow the directions below. If not, you can skip the next part. 

To create secrets.py:

First, navigate to the directory where all the files are.

```cmd
touch secrets.py
```

In secrets.py:

```python
pw = <yourPassword>
```

To run the program you must navigate into the directory where the file you want to run is stored and write:

```cmd
python <fileName.py>
```

To run in interactive mode write:

```cmd
python -i <filename.py>
```

## Methods

Below are the various methods in the program. Each on has a description detailing what it does and the parameters it takes. Use this to understand each one and user the ones you need, motify existing ones, or add new ones.

1. 
```python
def __init__(self, username, password)
```

or...

```python
def __init__(self, username)
```

This method is the first method to execute. It logs into Instagram with the username and pasword you passed in. If the username or password is incorrect, this will fail and the rest of the script will fail. If you create a sectrets.py file use the first one, if you pass in your password in the method, use the latter.

2. 
```python
def get_before_stats(self)
```

This method gets various stats of your profile before the script does its thing. It collects:

- number of posts
- number of followers
- number of users you follow
- list of every user by username you follow
- list of every user by username who follows you

3. 
```python
def get_before_stats(self)
```

This method gets various stats of your profile after the script does its thing. It collects:

- number of posts
- number of followers
- number of users you follow
- list of every user by username you follow
- list of every user by username who follows you

## Built With

- Python3 - Programming language used
- Selenium - Main Python library used

## Author

- [Benjamin Carlson](https://benjamincarlson.net)

## License

This project is under the MIT License -- see LICENSE.md for details
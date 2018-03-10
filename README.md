# Pyramid Based Journal
---
### Description
Version: *1.0.1*

My Personal Blog Page

* *You can access it* [here](https://chrisclosser.herokuapp.com)

### Author
---
* [Chris Closser](https://github.com/ChristopherSClosser/pyramid-learning-journal)

### Dependencies
---
* See requirements.txt

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/ChristopherSClosser/pyramid-learning-journal.git`

`$ cd pyramid-learning-journal`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`

##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command at the root level of your application, at the same level as development.ini and production.ini.

`$ pserve development.ini`

Once you have executed this command, open your browser, and go to `localhost:6543/`.

### Test Suite
---
##### *Running Tests*
This application uses [pytest](https://docs.pytest.org/en/latest/) as a testing suite. To run tests, run:

``$ pytest``

To view test coverage, run:

``$ pytest --cov``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./pyramid_learning_journal/tests.py` | Test learning journal. |
| `./pyramid_learning_journal/conftest.py` | Setup for tests. |

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| ./pyramid_learning_journal/routes.py | Define routes. |

### Pyramid Development Files
---
Development files specific to the Pyramid web framework can be found in the following files:
* ./development.ini

### Development Tools
---
* *python* - programming language
* *psycopg2* - DB management system
* *pyramid* - web framework
* *passlib* - security management
* *ipython* - command shell
* *pytest* - testing suite

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.

### Acknowledgements
---

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*

<pre>
//
--------------STEP3 TESTING---------------
//
//
(ENV)[chris-Studio-1558]~/CodeFellows/python/pyramid-learning-journal[step3 !?]:
$ pytest --cov --cov-report term-missing
============================= test session starts ==============================
platform linux -- Python 3.5.2, pytest-3.3.1, py-1.5.2, pluggy-0.6.0
rootdir: /home/chris/CodeFellows/python/pyramid-learning-journal,
inifile: pytest.ini
plugins: cov-2.5.1
collected 26 items
pyramid_learning_journal/tests.py..........................             [100%]
----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                         Stmts   Miss
Cover   Missing
pyramid_learning_journal/models/mymodel.py       8      0  100%
pyramid_learning_journal/views/default.py       26      0  100%
TOTAL                                           34      0  100%
========================== 26 passed in 4.15 seconds ===========================
//
//
//
-------------STEP4 TESTING------------
//
//
(ENV) [chris-Studio-1558]~/CodeFellows/python/pyramid-learning-journal[step4]:
$ pytest --cov --cov-report term-missing
============================= test session starts ==============================
platform linux -- Python 3.5.2, pytest-3.3.1, py-1.5.2, pluggy-0.6.0
rootdir: /home/chris/CodeFellows/python/pyramid-learning-journal,
inifile: pytest.ini
plugins: cov-2.5.1
collected 28 items
pyramid_learning_journal/tests.py ............................    [100%]
----------- coverage: platform linux, python 3.5.2-final-0 -----------
Name                                         Stmts   Miss  Cover Missing
pyramid_learning_journal/models/mymodel.py       8      0   100%
pyramid_learning_journal/views/default.py       34      0   100%
TOTAL                                           42      0   100%
========================== 28 passed in 5.36 seconds ===========================
</pre>

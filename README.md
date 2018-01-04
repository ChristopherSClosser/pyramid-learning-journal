# pyramid-learning-journal
---
### Description
Version: *0.1*

pyramid-learning-journal

### Authors
---
* https://github.com/ChristopherSClosser/pyramid-learning-journal

### Dependencies
---
* paster
* models
* deploy
* common
* response
* waitress
* config
* transaction
* view

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

`$ pserve development.ini`

Open your browser to http://localhost:6543

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
| `./pyramid_learning_journal/tests.py` | Journal tests. |

### Development Tools
---
* *python* - programming language
* *psycopg2* - DB management system
* *pyramid* - web framework

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*

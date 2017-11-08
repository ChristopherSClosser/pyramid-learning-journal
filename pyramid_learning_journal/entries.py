"""Hold the blog entries."""

ENTRIES = [
    {
    'title': "Day 16"
'text': "### Today I learned: - For Heroku: - enables use of https and serving css - in production: - change [app:main] to [app:pyramid_learning_journal] - above [server:main]add: - [filter:paste_prefix] - use = egg:PasteDeploy#prefix - [pipeline:main] - pipeline = - paste_prefix pyramid_learning_journal - in requirements add: - psycopg2==2.7.3 - pytest==3.2.3",
'created': "2017-11-07T13:56:38.085925",
'id': 976,
'markdown': "<h3>Today I learned:</h3> <ul> <li> <p>For Heroku:</p> <ul> <li>enables use of https and serving css</li> <li> <p>in production:</p> <ul> <li>change [app:main] to [app:pyramid_learning_journal]</li> <li> <p>above [server:main]add:</p> <ul> <li> <p>[filter:paste_prefix]</p> <ul> <li>use = egg:PasteDeploy#prefix</li> </ul> </li> <li> <p>[pipeline:main]</p> <ul> <li>pipeline =</li> <li>paste_prefix pyramid_learning_journal</li> </ul> </li> </ul> </li> </ul> </li> <li> <p>in requirements add:</p> <ul> <li>psycopg2==2.7.3</li> <li>pytest==3.2.3</li> </ul> </li> </ul> </li> </ul>",
'author': {
'display_name': "ChristopherSClosser",
'id': 45,
'username': "ChristopherSClosser",
'course_id': [
"sea401d7"
]
},
},
    {
        'title': "Day 13",
        'text': "### Today I learned: - Implement priority queue - SQLAlchemy (avoid sql injection security risk) - object relational mapper (translation layer your code --> SQL) - models/mymodels.py -- import models in models/__init__ - in model import Unicode Float DateTime - add correct Columns - set create date.now() in __init__ for model class - add and commit to get it in your db - many query methods - initializedb.py ---line 38:--- Base.metadata.drop_all(engine) - initdb development.ini - set in ENV/bin/activate export DATABASE_URL=' postgres://localhost:5432/learning_journal' - os.eviron[DATABASE_URL] - remove from development.ini and production - update __init__.py settings['sqlalchemy.url'] = os.eviron[DATABASE_URL] - then initializedb.py same line",
        'author': {
            'course_id': [
                "sea401d7"
                ],
        'username': "ChristopherSClosser",
        'id': 45,
        'display_name': "ChristopherSClosser"
        },
        'id': 893,
        'markdown': "<h3>Today I learned:</h3> <ul> <li>Implement priority queue</li> <li>SQLAlchemy (avoid sql injection security risk)<ul> <li>object relational mapper (translation layer your code --&gt; SQL)</li> </ul> </li> <li>models/mymodels.py -- import models in models/<strong>init</strong></li> <li>in model import Unicode Float DateTime<ul> <li>add correct Columns</li> <li>set create date.now() in <strong>init</strong> for model class</li> </ul> </li> <li>add and commit to get it in your db</li> <li>many query methods</li> <li>initializedb.py ---line 38:--- Base.metadata.drop_all(engine)<ul> <li>initdb development.ini</li> </ul> </li> <li>set in ENV/bin/activate export DATABASE_URL=' postgres://localhost:5432/learning_journal'</li> <li>os.eviron[DATABASE_URL]</li> <li>remove from development.ini and production</li> <li>update <strong>init</strong>.py settings['sqlalchemy.url'] = os.eviron[DATABASE_URL]<ul> <li>then initializedb.py same line</li> </ul> </li> </ul>",
        'created': "2017-11-02T01:20:34.210642"
    },
    {
        'title': "Day 12",
        'text': "### Today I learned - Binary heap min and max - Start to Implement max heap - Using jinja2 templates - MVC - Pyramid Renderers - Group project selection",
        'author': {
            'course_id': [
            "sea401d7"
            ],
            'username': "ChristopherSClosser",
            'id': 45,
            'display_name': "ChristopherSClosser"
        },
        'id': 888,
        'markdown': "<h3>Today I learned</h3> <ul> <li>Binary heap min and max<ul> <li>Start to Implement max heap</li> </ul> </li> <li>Using jinja2 templates</li> <li>MVC</li> <li>Pyramid Renderers</li> <li>Group project selection</li> </ul>",
        'created': "2017-11-01T15:33:24.823650"
},
{
'title': "Day 11",
'text': "### Today I learned: - pyramid and templating - algorythms - if there is recursion or iteration not O(1) - T(n)=3+3n2+2n+1=3n2+2n+4T(n)=3+3n2+2n+1=3n2+2n+4 - By looking at the exponents, see that the n2n2 term will be dominant this code is O(n2) (a nested loop). - sorting is typically either O(n2)O(n2) or O(nlogn)",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 859,
'markdown': "<h3>Today I learned:</h3> <ul> <li>pyramid and templating</li> <li>algorythms - if there is recursion or iteration not O(1)</li> <li>T(n)=3+3n2+2n+1=3n2+2n+4T(n)=3+3n2+2n+1=3n2+2n+4<ul> <li>By looking at the exponents, see that the n2n2 term will be dominant this code is O(n2) (a nested loop).</li> </ul> </li> <li>sorting is typically either O(n2)O(n2) or O(nlogn)</li> </ul>",
'created': "2017-10-31T15:29:21.627417"
},
{
'title': "Day 10",
'text': "### Today I learned: - put testing fixtures in conftest.py - find out if a linked list is circular - to have a lot of patience - git hub issues - if string is anagram",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 840,
'markdown': "<h3>Today I learned:</h3> <ul> <li>put testing fixtures in conftest.py</li> <li>find out if a linked list is circular</li> <li>to have a lot of patience </li> <li>git hub issues</li> <li>if string is anagram</li> </ul>",
'created': "2017-10-28T17:09:17.436370"
},
{
'title': "Day 9",
'text': "### Today I learned: - Make a queue first in first out - concurrency in python using gevent - getters and setters class methods - define property of class (makes it read only) @property - networking get your face out and meet people who have similar interests",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 816,
'markdown': "<h3>Today I learned:</h3> <ul> <li>Make a queue first in first out</li> <li>concurrency in python using gevent</li> <li>getters and setters class methods</li> <li>define property of class (makes it read only) @property</li> <li>networking get your face out and meet people who have similar interests</li> </ul>",
'created': "2017-10-27T15:17:27.732450"
},
{
'title': "Day 8",
'text': "#### Today I learned: - string to make module use unicode strings # -*- coding: utf-8 -*- - using pytest fixtures for testing you can put fixtures in conftest.py - fixture scope - - function - class - module - session - white boarding a linked-list zip function - class inheritance and using super to keep and modify main class methods",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 788,
'markdown': "<h4>Today I learned:</h4> <ul> <li>string to make module use unicode strings # -<em>- coding: utf-8 -</em>-</li> <li>using pytest fixtures for testing you can put fixtures in conftest.py<ul> <li>fixture scope -<ul> <li>function</li> <li>class</li> <li>module</li> <li>session</li> </ul> </li> </ul> </li> <li>white boarding a linked-list zip function</li> <li>class inheritance and using super to keep and modify main class methods</li> </ul>",
'created': "2017-10-26T15:24:10.465579"
},
{
'title': "Day 7:",
'text': "#### Today I learned: - HTTP protocalls - request and response headers - Methods (CRUD) - Class inheritance - Data structures - Linked list implementation - Implement a stack inherit from LinkedList",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 761,
'markdown': "<h4>Today I learned:</h4> <ul> <li>HTTP protocalls<ul> <li>request and response headers</li> <li>Methods (CRUD)</li> </ul> </li> <li>Class inheritance</li> <li>Data structures <ul> <li>Linked list implementation</li> <li>Implement a stack inherit from LinkedList</li> </ul> </li> </ul>",
'created': "2017-10-25T15:19:01.943580"
},
{
'title': "Day 6",
'text': "### Today I learned: - Class construction - Methods for classes - Replace built-in methods in a class - Simple echo server setup",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 735,
'markdown': "<h3>Today I learned:</h3> <ul> <li>Class construction</li> <li>Methods for classes </li> <li>Replace built-in methods in a class</li> <li>Simple echo server setup</li> </ul>",
'created': "2017-10-24T15:26:47.944662"
},
{
'title': "Day of code",
'text': "I methodically went through this assignment and hopefully learned some good habits when it comes to updating the readme and testing.",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 694,
'markdown': "<p>I methodically went through this assignment and hopefully learned some good habits when it comes to updating the readme and testing.</p>",
'created': "2017-10-22T02:56:29.580689"
},
{
'title': "Day 4",
'text': "#### Today I Learned: * make a list of errors from \__builtin__: err_list = [name for name in dir\(\__builtin__) if "'Error'" in name] * list, tuple, and dictionary methods: In [29]: list('blahblah') Out[29]: ['b', 'l', 'a', 'h', 'b', 'l', 'a', 'h'] In [30]: tuple({1: 'a',2: 'b',3: 'c','a': 1,'b': 2,'c': 3}.items()) Out[30]: ((1, 'a'), (2, 'b'), (3, 'c'), ('c', 3), ('b', 2), ('a', 1)) * try: except statements and how to raise custom errors * lambdas",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 659,
'markdown': "<h4>Today I Learned:</h4> <ul> <li> <p>make a list of errors from __builtin__:</p> <div class="'codehilite'"><pre> err_list = [name for name in dir\(\__builtin__) if &quot;Error&quot; in name] </pre></div> </li> <li> <p>list, tuple, and dictionary methods:</p> <div class="'codehilite'"><pre>In [29]: list(&#39;blahblah&#39;)<br>Out[29]: [&#39;b&#39;, &#39;l&#39;, &#39;a&#39;, &#39;h&#39;, &#39;b&#39;, &#39;l&#39;, &#39;a&#39;, &#39;h&#39;]<br>In [30]: tuple({1: &#39;a&#39;,2: &#39;b&#39;,3: &#39;c&#39;,&#39;a&#39;: 1,&#39;b&#39;: 2,&#39;c&#39;: 3}.items())<br>Out[30]: ((1, &#39;a&#39;), (2, &#39;b&#39;), (3, &#39;c&#39;), (&#39;c&#39;, 3), (&#39;b&#39;, 2), (&#39;a&#39;, 1)) </pre></div> </li> <li> <p>try: except statements and how to raise custom errors</p> </li> <li>lambdas</li> </ul>",
'created': "2017-10-21T03:34:49.189437"
},
{
'title': "Day 3",
'text': "# Today I Learned... * More about dictionaries, non indexed * Sets ([1,2,3]) ignore duplicates and are non indexed * How to create .coveragerc * Slicing and the : and :: operators * The --verbose flag for testing * Dealing with files * Using setuptools",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 631,
'markdown': "<h1>Today I Learned...</h1> <ul> <li>More about dictionaries, non indexed</li> <li>Sets ([1,2,3]) ignore duplicates and are non indexed</li> <li>How to create .coveragerc</li> <li>Slicing and the : and :: operators</li> <li>The --verbose flag for testing</li> <li>Dealing with files</li> <li>Using setuptools</li> </ul>",
'created': "2017-10-20T00:57:40.407555"
},
{
'title': "Week 1 day 2:",
'text': "- I learned a lot about booleans, - how to ping pong pair program, - how to run certain things if from the command line, - test driven pythoning, - how to set up environments, - args and kwargs, - I could keep going...",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 604,
'markdown': "<ul> <li>I learned a lot about booleans,</li> <li>how to ping pong pair program,</li> <li>how to run certain things if from the command line,</li> <li>test driven pythoning,</li> <li>how to set up environments,</li> <li>args and kwargs,</li> <li>I could keep going...</li> </ul>",
'created': "2017-10-18T00:34:49.412531"
},
{
'title': "Stuff I learned today",
'text': "I am a software craftsman python 3 str is utf-8 unicode python 2 division of integers results in a floored integer python 2 division of a float and an integer results in a float python 3 division of all integers results in a float try not to mutate from inside functions instead return new objects a tuple is a list of immutable objects e.g. my_tuple = () with only one object my_tuple = (1,)",
'author': {
'course_id': [
"sea401d7"
],
'username': "ChristopherSClosser",
'id': 45,
'display_name': "ChristopherSClosser"
},
'id': 592,
'markdown': "<p>I am a software craftsman</p> <p>python 3 str is utf-8 unicode python 2 division of integers results in a floored integer python 2 division of a float and an integer results in a float python 3 division of all integers results in a float</p> <p>try not to mutate from inside functions instead return new objects a tuple is a list of immutable objects e.g. my_tuple = () with only one object my_tuple = (1,)</p>",
'created': "2017-10-17T12:49:02.615079"
}
]

cleverbotio.py
============

A python wrapper for the cleverbot.io API that has an async option
============
Note: This is WIP


Example
-------

.. code:: py

    import Cleverbotio


    cb = Cleverbotio.Cleverbot('API_USER','YOUR_API_KEY', 'Bot Nickname)
    
    cb.create_session()
    resp = cb.say("Hello World")
    
    print(resp)
    # will print something like: {'status': 'success', 'response': "I'm not the world."}

Installing
----------

Install it normally from `PyPI <https://pypi.org/project/cleverbotio/>`_ with
pip:

::

    pip install cleverbotio

Or install it with the asynchronous dependencies (Python 3.4.2+ only):

::

    pip install cleverbotio[async]

**Requirements:**

- Python 3.2+ or 2.7
- `A Cleverbot API Key <https://cleverbot.io/login>`_

**Dependencies:**

- requests 1.0.0+

+ **Asynchronous:**

  - aiohttp 1.0.0+

Usage
-----

First import the package:

.. code:: py

    import Cleverbotio

If you have the asynchronous dependencies and want to use Cleverbot
asynchronously import it as below instead:

.. code:: py

    from Cleverbot import async as cleverbot

Then initialize Cleverbot with your API key and optionally a cleverbot state,
timeout and or tweak if you want to adjust Cleverbot's mood:

.. code:: py

    cb = Cleverbot.Cleverbot('API_USER, 'YOUR_API_KEY', 'Bot Nickname')
    
Now you create a cleverbot instance

.. code:: py
     
    cb.create_session

Now you can use the say function which returns a JSON dict from the API of the status and cleverbot response

.. code:: py

    resp = cb.say('Hello World')
    print(resp)
    #should print a dict like: {'status': 'success', 'response': "I'm not the world."}
   

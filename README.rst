Lights
======
Short description


**What is this repository for?**


How do I get set up?
--------------------

* Summary of set up
* Configuration
* Dependencies


Install python, pip, virtualenv, virtualenvwrapper

Install git, clone repo.

create virtualenv, setvirtualenvproject, pip install -r requirements.txt

Copy .env.redacted to .env, edit file adding secret keys and account settings.
To generate django key:

code-block:: python
	import string
	from django.utils.crypto import get_random_string

	get_random_string(50, string.letters + string.digits + string.punctuation)

TODO: Add all the steps I took to get this thing working on the devbox. 
install vagrant, virtualbox, ansible
install postgresql, postgis...

Deployment instructions
-----------------------


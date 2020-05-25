# Installation


## Installation and Configuration

**Make directory called ap_reporting.**

    $ mkdir ap_reporting

`**cd**` **into ap_reporting**

    $ cd ap_reporting

**Clone this repository.**

    $ git clone {url} ap_reporting

**Make** `**virtualenv**` **for this repo.**
Inside your ap_reporting directory

    $ virtualenv --python=`which python` env
    $ source env/bin/activate

**Install all the dependencies.**

    (env) $ cd ap_reporting
    (env) $ pip install -r requirements.txt

**Run the project**

    (ap_reporting) $ gunicorn --bind=0.0.0.0:5000 wsgi:app
## AWS Configurations
    WSGIPath: run.py 
    Static Directory: ap_reporting/static/ 
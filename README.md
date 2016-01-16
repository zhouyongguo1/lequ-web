## Prerequisites

* Python 3.4 or higher
* Python virtualenv
* node 0.10
* MySQL(percona-server) 5.6 or higher
* redis


### Create a virtualenv

    $ mkvirtualenv -p `which python3` lequ

 or

    $ virtualenv -p `which python3` ~/.virtualenvs/lequ
    $ source activate           # activate the virtualenv we just created

## create db
    $ git clone git@github.com:zhouyongguo1/lequ-db.git
    $ cd lequ-db
    $ mysql> create database lequ_dev character set utf8;
    $ mysql> create database lequ_test character set utf8;
    $ ./reset
   
## Install node and dependencies
    
### Install node
    # Mac user
    brew install node
    
### Install gulp
    $ npm install -g gulp
    
### Start asset watcher
    $ gulp


### Create install model
    $ pip install -r requirements
    $ pip freeze > requirements.txt
    
    
### Run
    $ workon lequ
    $ python run.py



    
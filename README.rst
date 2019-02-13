The python version for cobot
============================

Download
--------
    git clone https://github.com/victoryang/cobot-python

Prequisite
----------
    pip
    twine

Setup tools
-----------
    pip install setuptools twine
    
    python setup.py sdist

Install
-------
    pip install ./dist/cobot-python-0.1.tar.gz

Upload
------
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    
    pip install --index-url https://test.pypi.org/simple/

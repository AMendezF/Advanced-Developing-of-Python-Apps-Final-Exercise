#  Advanced-Developing-of-Python-Apps-Final-Exercise

This is an exercise that I did for a python advanced learning course.

The exercise is divided into two parts:
 
- A python **REST** app, that has several **POST** endpoints that only accepts a **JSON** input. Otherwise, returns HTTP 500 error. The endpoints are:

    - **/suma/** , adds element-wise the JSON float lists and returns the result as HTTP response.
    - **/resta/** , subtracts element-wise the JSON float lists and returns the result as HTTP response.
    - **/mult/** , multiplies element-wise the JSON float lists and returns the result as HTTP response.
    - **/divis/** , divides element-wise the JSON float lists and returns the result as HTTP response.

- A python module, that has a class with all the operation functions to make the endpoints work. 

JSON input should be in the form:
```python
{'v1': type.List[float], 'v2': type.List[float]}.
```

The python module is named **calclib**. It contains a float vector calculator with safe input check. Also, has unittest tests and Sphinx documentation source files.

## Installation

Ensure that an up-to-date version of setuptools is installed:

```sh
$ python3 -m pip install --upgrade setuptools
```

To install the module:

```sh
$ cd calclib_packaging
$ python3 setup.py sdist
$ pip3 install dist/calclib-1.0.tar.gz
```

To run app.py, **flask** is needed:

```sh
$ pip3 install -U flask
```

Then:

```sh
$ python3 -m flask run
```

## Test (**calclib**)

```sh
$ cd calclib_packaging
$ python3 setup.py test
```

## Documentation (**calclib**)

Need [Sphinx](www.sphinx-doc.org) and furo :
```sh
$ pip3 install sphinx furo
```

To generate documentation:

```sh
$ cd calclib_packaging/docs
$ make html
```


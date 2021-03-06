# Contributing to Django Extensions

There are many ways to contribute to the project. You may improve the documentation, address a bug, add some feature to the code or do something else. All sort of contributions are welcome.

## Development

To start development on this project, fork this repository and follow the following instructions.

```bash
# clone the forked repository
$ git clone YOUR_FORKED_REPO_URL

# create a virtual environment
$ python3 -m venv venv
# activate the virtual environment
$ source venv/bin/activate
# install django-extensions in development mode
(venv) $ pip install -e .
# install dependencies
(venv) $ pip install Django -r requirements-dev.txt

# for accessing the GUI portion of the test application
(venv) $ export DJANGO_EXTENSIONS_DATABASE_NAME="db.sqlite3"    # you may change if you want to use any other database
# start the development server
(venv) $ python manage.py runserver
```

### Pre-Commit

To improve code quality install pre-commit to perform precommit checks before push code to GitHub.

```bash
# Install pre-commit
(venv) $ pip install pre-commit
# Run pre-commit install to setup the git hook scripts
(venv) $ pre-commit install
```

### Testing

To run tests against a particular `python` and `django` version installed inside your virtual environment, you may use:

```bash
# install pytest
(venv) $ pip install pytest-django # `python manage.py test` or `make test` also work
(venv) $ pytest # `python manage.py test` or `make test` also
```

To run tests against all supported `python` and `django` versions, you may run:

```bash
# install dependency
(venv) $ pip install tox
# run tests
(venv) $ tox
```

### Documentation

The project uses the Numpy Docstring standard to document code and is build using sphinx.
To generate documentation you may run the following commands:

```bash
# install dependency
(venv) $ pip install sphinx
# build new docs from source
(venv) $ sphinx-apidoc -f -o docs/source actina/
# Generate new site from docs
(venv) $ sphinx-build -b html docs/source/ docs/build/html

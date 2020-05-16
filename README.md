# foodle

## Development

After `git clone` and `cd` into the project directory, enter the following
code to initialze development environment:

```shell
# install python 3.8.3
pyenv install 3.8.3

# create virtualenv based on python 3.8.3
pyenv virtualenv 3.8.3 foodle

# specify the virtualenv just created
pyenv local foodle

# install package manager
pip install --upgrade pip
pip install poetry

# install project dependencies
poetry install
pyenv rehash

# install pre-commit hook
pre-commit install
```

Now you are ready to perform routinely development process:

```shell
# install project dependencies
poetry install
pyenv rehash

# perform db migration
./manage.py migrate

# run devserver
./manage.py runserver
```

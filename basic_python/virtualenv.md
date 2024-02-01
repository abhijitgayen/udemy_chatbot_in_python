We use a module named virtualenv which is a tool to create virtual environments in Python, isolated from system environment Python.

virtualenv creates a folder that contains all the necessary executables to use the packages that a Python project would need.

## Install virtualenv

```
pip install virtualenv
```

## Version test

```
virtualenv --version
```

## Create virtual environment

```
python3 -m venv myenv
```

## Activate virtual environment

### For Windows:

```
myenv\Scripts\activate
```

### For macOS and Linux:

```
source myenv/bin/activate
```

# deactivate virtual environment

```
deactivate
```

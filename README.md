# KroniaBackend

Contains the backend code for Kronia

## Running application

To start the application and the backend instances, run the following commands:

### Setting up .env ```PytorchAnnual/```

- Create a ```.env``` file.
To enable our basic setup environment, let’s add some information
```
api_endpoint="Enter your plant-net classifier API"
```

* Make sure to have python 3 installed
* Create a virtual environment by running ``` virtualenv venv -p python3 ```
* Activate the virtual environment by running ```source venv/bin/activate```
* Install required dependencies by running ```pip install -r requirements.txt```
* Run the app by running ```python app.py```

## Primary Frameworks

* Flask
* plant-net
* torch
* torchvision
* numpy
* pandas
* dot-env

Raise issues and submit PRs if you think something could be better!

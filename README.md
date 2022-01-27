# NBA Challenge
This is a python test. The idea is to create a function that get the pair of the nba players. The script run with Python 3  

# Steps

# PART I: Clone repository and install dependencies
```
//on local
git clone https://github.com/diegovallel/nbaPlayerTest.git
```
# install the libraries
```
pip install -r requirements.txt
```

# PART II: Run the app
To test the app, There are two ways:

# Run Script 

## Steps for local script

## PART I: Run script
Inside the folder there is an script called testNbaPlayers.py. This file have the script to make the pair height players. Once the script is run, there is going to appear a message in the console asking for a height:

```
python3 testNbaPlayers.py
```
```
Please enter the height to match:
```

Once the input is inserted, the script would return the result (the pair players height).

## Steps for API

## PART I: Endpoint

The other way to run the script is by an API developed with Fast API.

To run the project, go to the folder app and run the next commands:

In order to create a virtual env.
```
mkdir venv; cd venv
```
```
virtualenv -p python3 virtual
```
```
source virtual/bin/activate
```

With the vitual enviroment activated, go back to the app folder and run the next command:

```
uvicorn main:app --reload
```

With this, now the endpoint is live. The endpoint path is:

<strong> Api-Service: </strong>
- /api/v1/nbaPlayers


## PART II: Test the endpoints

There are two ways to test the apps. For postman or swagger.

To have access to swagger, once run `uvicorn main:app --reload`, use the next url for api:

`http://localhost:8000/docs`

<strong>Thank you!!</strong>
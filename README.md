<h1 align="center">Welcome to financial calculator backend 👋</h1>
<p>
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/wanderindev/financial-calculator-backend/blob/master/README.md">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/financial-calculator-backend/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://htmlpreview.github.io/?https://github.com/wanderindev/financial-calculator-backend/blob/master/htmlcov/index.html">
    <img alt="Coverage" src="https://img.shields.io/badge/coverage-98%25-green.svg" target="_blank" />
  </a>  
  <a href="https://github.com/wanderindev/financial-calculator-backend/blob/master/LICENSE.md">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/JavierFeliuA">
    <img alt="Twitter: JavierFeliuA" src="https://img.shields.io/twitter/follow/JavierFeliuA.svg?style=social" target="_blank" />
  </a>
</p>

## About
This project contains an API for a financial calculator.  I coded this project in Python, using Flask and NumPy.

In conjunction with the [Financial Calculator Frontend](https://github.com/wanderindev/financial-calculator-frontend), this project provides a companion calculator for the personal finance book ["Mejora Tu Situación."](https://www.amazon.com/Mejora-ituaci%C3%B3n-necesitas-personales-calcularlo-ebook/dp/B08DN9L7V9?_encoding=UTF8&camp=1789&creative=9325&linkCode=ur2&tag=storypodca-20&linkId=2P4S6EY6B462X4AR)  

### Design Considerations
For this project, the book author presented me with a series of calculators built on MS Excel.  The goal was to produce an online calculator that, given the same inputs, would return the same results as the Excel samples.

Most of Excel's financial formulas have the calculation method obfuscated.  That is, you can't see how it arrives at the result.  

The Python library NumPy contains 1:1 equivalents to all of Excel's financial formulas.  For this reason, I decided to break up the problem into two: 
1. **(This repository)** An API in Python would receive the calculation parameters from the frontend and return the results calculated with NumPy.
2. **([The frontend repository](https://github.com/wanderindev/financial-calculator-frontend))** A frontend would provide a user interface for receiving calculation parameters and presenting the results.

### Important links
1. You can take a look at the frontend code [here](https://github.com/wanderindev/financial-calculator-frontend).
2. Find the live calculator [here](https://www.calcfina.com/es/calculadora-de-ahorros.html).
3. The live backend is [here](https://api.calcfina.com).  The API is open, so you can test it using Postman (see the Postman section below for instructions).
4. This project runs in a Kubernetes cluster at DigitalOcean.  For information on how to create your cluster visit my [do-managed-kubernetes](https://github.com/wanderindev/do-managed-kubernetes) repository.

## Install
To use the project in your development machine, clone it, and go to the project's root:
```sh
git clone https://github.com/wanderindev/financial-calculator-backend.git
cd financial-calculator-backend
```
From the project's root, create and activate your virtual environment:
```sh
python3 -m venv venv
. venv/bin/activate
```
And install the project's dependencies:
```sh
pip install -r requirements.txt
```

## Development
During develpment use:
```sh
docker-compose up --build
```
to create a container running the backend.  Access the container at `http://localhost:5001`

Modify the code as needed and test using Postman (see instructions below), sending requests to the container running at localhost.

The ```calculators``` package contains all de classes for the different financial calculators. 

The ```resources``` package contains all the endpoints

### Postman
Import `fc-backend.postman_collection.json` into Postman for a collection of all endpoints.

Add a `url` variable to the environment with value `http://localhost:5001` for development.  Make sure you have a container running the backend as per instructions above before sending requests.

To test against the live backend, add a `url` variable to the Postman environment with value `https://api.calcfina.com` and send your requests.

### Tests
To insure code quality, I added UnitTest to the project.  All tests all located in the ```tests``` package.  

To test the project, make sure your virtual environment is activated and run:
```sh
python -m unittest tests/test_credit_card_calculators.py tests/test_loan_calculators.py tests/test_retirement_calculators.py tests/test_saving_calculators.py
```
The included tests provide 98% coverage for the codebase.  You can find the coverage report [here](https://htmlpreview.github.io/?https://github.com/wanderindev/financial-calculator-backend/blob/master/htmlcov/index.html).

## Deployment

Before deployment, you have to replace the SECRET_KEY in line 32 of the Dockerfile for something, well, secret.  **Make sure you don't commit the modified Dockerfile to version control**.

Next, you need to build the Docker image for the project and push it to your Docker Hub account:
```sh
docker build -t wanderindev/fc-backend .
docker push wanderindev/fc-backend
```
Replace ```wanderindev``` above (my Docker Hub account id) with your Docker Hub id.

Then, from the root of [do-managed-kubernetes](https://github.com/wanderindev/do-managed-kubernetes) project run:
```sh
kubectl delete deployment fc-backend
kubectl apply -f ./python/fc-backend.yml
```
to create two pods running the backend and a service exposing them at port 80.

For more information on deploying to a Kubernetes cluster, visit 
my [do-managed-kubernetes](https://github.com/wanderindev/do-managed-kubernetes) repository.

## Author

👤 **Javier Feliu**

* Twitter: [@JavierFeliuA](https://twitter.com/JavierFeliuA)
* Blog: [Wander In Dev](https://wanderin.dev)
* Github: [@wanderindev](https://github.com/wanderindev)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](https://github.com/wanderindev/financial-calculator-backend/blob/master/LICENSE.md) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

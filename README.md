<h1 align="center">Welcome to financial calculator backend 👋</h1>
<p>
  <img src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/wanderindev/financial-calculator-backend/blob/master/README.md">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/financial-calculator-backend/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/financial-calculator-backend/blob/master/LICENSE.md">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/JavierFeliuA">
    <img alt="Twitter: JavierFeliuA" src="https://img.shields.io/twitter/follow/JavierFeliuA.svg?style=social" target="_blank" />
  </a>
</p>

> Python backend for [financial calculator](https://fc-frontend.wanderin.dev)


## Install

```sh
git clone https://github.com/wanderindev/financial-calculator-backend.git
cd financial-calculator-backend
```

## Usage
During develpment use:
```sh
docker-compose up --build
```
to create a container running the backend.  Access the container at `http://localhost:5001`

For deployment:

Replace the SECRET_KEY in line 32 of Dockerfile and run:
```sh
docker build -t wanderindev/fc-backend .
docker push wanderindev/fc-backend
```
Then, from the root of do-kubernetes project:
```sh
kubectl delete deployment fc-backend
kubectl apply -f ./python/fc-backend.yml
```
to create two pods running the backend and a service exposing them at port 80.

For more information on deploying to a Kubernetes cluster, visit 
my [do-managed-kubernetes](https://github.com/wanderindev/do-managed-kubernetes) repository.

For information on the financial calculator frontend, visit 
my [financial-calculator-frontend](https://github.com/wanderindev/financial-calculator-frontend) repository.

## Postman
Import `fc-backend.postman_collection.json` into Postman for a collection of all endpoints.

Add a `url` variable to the environment with value `http://localhost:5001` for development or
`https://fc-backend.wanderin.dev` for production.

## Author

👤 **Javier Feliu**

* Twitter: [@JavierFeliuA](https://twitter.com/JavierFeliuA)
* Github: [@wanderindev](https://github.com/wanderindev)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](https://github.com/wanderindev/financial-calculator-backend/blob/master/LICENSE.md) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

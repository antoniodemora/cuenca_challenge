# Cuenca Challenge

This is the coding challenge from cuenca

## Getting started

Dependencies:

- [Python 3.7+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/)


## Installation

Setup your environment with:

```sh
git clone <git_repo>
cd cuenca_challenge
docker build .
docker-compose build
```

## Testing

To run the tests, just execute:

```sh
docker-compose run cuenca_challenge sh -c "python ./tests.py"
```

To store the solutions to the database, execute:

```sh
docker-compose run cuenca_challenge sh -c "python ./nqueen.py"
```
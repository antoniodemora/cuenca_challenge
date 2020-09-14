# Cuenca Challenge

This is the coding challenge from cuenca:

1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
2. iterate over N and store the solutions in postgres using SQLAlchemy
3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

This solution is taken from this [approach](https://github.com/snazrul1/PyRevolution/blob/master/Puzzles/N_Queen_Problem.ipynb) which is very simple and pythonista, using permutations, sets and list comprehension to find the solutions.

## Getting started

Dependencies:

- [Python 3.6+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/)
- [Git](https://git-scm.com/)

## Installation

Setup your environment with:

```sh
git clone git@github.com:antoniodemora/cuenca_challenge.git
cd cuenca_challenge
docker build .
docker-compose build
```

## Testing

To run the tests, just execute:

```sh
docker-compose run cuenca_challenge sh -c "python ./tests.py"
```

## Running

To store the solutions to the database, execute:

```sh
docker-compose run cuenca_challenge sh -c "python ./nqueen.py"
```
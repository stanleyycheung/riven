# riven

Lightweight wrapper around Riot's API for League of Legends

Named after the legendary Koware's main champion

[![CI](https://github.com/stanleyycheung/riven/actions/workflows/ci.yml/badge.svg)](https://github.com/stanleyycheung/riven/actions/workflows/ci.yml)

## Setup

Create a file called `.env` in the base directory and put your Riot API key in a variable `RIOT_API_KEY`.

Install `pipenv` package and do `pipenv install` to install all the dependencies.

Run `./test/run_tests.sh` to run all tests. Require over 90% coverage for PR to be merged.

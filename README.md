# riven

Lightweight wrapper around Riot's API for League of Legends

Named after the legendary Koware's main champion

[![.github/workflows/ci.yml](https://github.com/stanleyycheung/riven/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/stanleyycheung/riven/actions/workflows/ci.yml)

## Setup

Create a file called `.env` in the base directory and put your Riot API key in a variable `RIOT_API_KEY`.

Install `poetry` and run `poetry install` to install all the dependencies.

Run `./test/run_tests.sh` to run all tests. Require over 90% coverage for PR to be merged.

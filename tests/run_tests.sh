#!/usr/bin/env bash

coverage run -m pytest
retVal=$?
if [ $retVal -ne 0 ]; then
    exit $retVal
fi
coverage html -d tests/coverage_html
coverage report -m --fail-under=90
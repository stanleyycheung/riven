#!/usr/bin/env bash

coverage run -m pytest --verbose
exitCode=$?
if [ $exitCode -ne 0 ]; then
    exit $exitCode
fi
coverage report --omit="tests/*" --fail-under=90
exitCode=$?
if [ $exitCode -ne 0 ]; then
    exit $exitCode
fi
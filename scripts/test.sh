#!/bin/sh

echo 'Preparing to run tests'
{
	docker run --rm --name team_rocket_app team_rocket_app python ./tests/test1.py
} || {
	echo 'Tests could not be run.'
	echo 'Report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'Tests have been successfully run'


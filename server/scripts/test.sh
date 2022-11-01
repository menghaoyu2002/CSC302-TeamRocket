#!/bin/sh

echo 'Preparing to run tests'
{
	docker run --rm --name team_rocket_server team_rocket_server pytest
} || {
	echo 'Tests could not be run.'
	echo 'Report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'Tests have been successfully run'


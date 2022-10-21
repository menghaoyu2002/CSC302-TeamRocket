#!/bin/sh

echo 'starting the application...'
{
	docker run --rm --name team_rocket_app team_rocket_app
} || {
	echo 'Failed. There was an issue running the application with its docker image.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}
echo 'Application finished running.'

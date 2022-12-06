#!/bin/sh

echo 'Preparing to run end to end tests'
{
	docker compose -f docker-compose.cypress.yml up --build --abort-on-container-exit
} || {
	echo 'end to end tests could not be run.'
	echo 'Report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'end to end tests have been successfully run'
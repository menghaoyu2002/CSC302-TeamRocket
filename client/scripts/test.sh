#!/bin/sh

echo 'Preparing to run client unit tests'
{
	docker run -e CI=true --rm --name csc302-teamrocket-client csc302-teamrocket-client npm test -- --coverage
} || {
	echo 'Client unit tests could not be run.'
	echo 'Report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'Client unit tests have been successfully run'
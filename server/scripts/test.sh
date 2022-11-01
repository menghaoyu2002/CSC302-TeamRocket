#!/bin/sh

echo 'Preparing to run server tests'
{
	docker run --rm --name csc302-teamrocket-server csc302-teamrocket-server pytest -v 
} || {
	echo 'Server tests could not be run.'
	echo 'Report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'Server tests have been successfully run'


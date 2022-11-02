#!/bin/sh

echo 'starting the server...'
{
	docker run -it -p 5000:5000 --rm  --name csc302-teamrocket-server csc302-teamrocket-server
	echo ""
} || {
	echo 'Failed. There was an issue running the server with its docker image.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'server finished running.'

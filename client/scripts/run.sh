#!/bin/sh

echo 'starting the client...'
{
	docker run -it -p 3000:3000 --rm --name csc302-teamrocket-client csc302-teamrocket-client
	echo ""
} || {
	echo 'Failed. There was an issue running the client with its docker image.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'client finished running.'
#!/bin/sh

echo 'building docker client image...'
{ 
	docker build -t csc302-teamrocket-client .
} || {
	echo 'docker build failed.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'build complete!'
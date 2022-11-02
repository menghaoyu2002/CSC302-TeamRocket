#!/bin/sh

echo 'building docker server image...'
{ 
	docker build -t csc302-teamrocket-server .
} || {
	echo 'docker build failed.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'build complete!'

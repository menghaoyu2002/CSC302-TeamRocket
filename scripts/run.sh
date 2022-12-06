#!/bin/sh
timestamp=$(date +%Y-%m-%dT%H:%M:%S%:z)
{
	mkdir -p ./logs
	docker compose up --build --abort-on-container-exit | tee ./logs/$timestamp.log
} || {
	echo 'Unable to run program.'
	echo 'Please report this issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with the log file:'
	echo ./logs/$timestamp.log
}
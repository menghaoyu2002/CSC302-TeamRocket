#!/bin/sh
timestamp=$(date +%Y-%m-%dT%H:%M:%S%:z)
{
	mkdir -p ./logs
	docker compose logs > ./logs/$timestamp.log
} || {
	echo "Logs were unable to be saved"
	echo "Make sure to save them manually from the 'docker compose logs' command."
}

#!/bin/sh

echo 'starting the client...'
{
	docker run -it -p 3000:3000 --rm --name team_rocket_client team_rocket_client
	echo ""
} || {
	echo 'Failed. There was an issue running the client with its docker image.'
	echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with your terminal output'
	exit 1
}

echo 'client finished running.'
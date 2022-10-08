# CSC302-TeamRocket

This setup assumes that you are in the root directory of our project, and will break if you are not.

NOTE: it is highly recommended that you run each of our shell scripts as follows where script.sh is the name of the script.

```bash
chmod +x ./scripts/*
sudo ./scripts/script.sh
```

For the sake of making the process of running each script a single command we have reduced it to one command. We also chose to omit the sudo command since it would be another dependency for us to manage.

Also note that our setup currently only supports Ubuntu, Debian, Fedora, CentOS. And only supports the package managers apt, dnt, and yum.

We chose to only support these OS because docker is only supported (without binaries) on CentOS, Debian, Fedora, Ubuntu, SLES, and RHEL. For the sake of supporting a more modern and commonly used linux, we chose to omit SLES and RHEL. Although the same setup works with Debian and Ubuntu derivatives, it seemed infeasible to manage such a large number of distros. We've handled this case via referring the user to the manual install page.

If your machine is running something else, you should get an informative error message telling you to install manually.

We have not handled the case where shell scripts cannot be run on the machine, i.e. sh is not available. This seemed like a unlikely situation seeing as that the machine could be assumed to be running a modern linux.

## Why is admin permissions required?

We need elevated permissions in order to install docker onto your machine. There is no way around it.

Futhermore, when docker is installed, elevated permissions are required to run any docker command. This is because the user is not yet added to the docker group, which would require another step, and even when automated, will still require the user to logout or restart the machine.

## Installing Dependencies

This script installs docker and all our dependencies.

```bash
su -c '. ./scripts/install.sh'
```

## Building the Application

This script builds our docker container.

```bash
su -c '. ./scripts/build.sh'
```

## Running the Application

This script runs our docker container, i.e. the application.

```bash
su -c '. ./scripts/run.sh'
```

## Running Tests

This script runs all our tests.

```bash
su -c '. ./scripts/test.sh'
```

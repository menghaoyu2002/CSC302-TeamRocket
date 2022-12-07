# CSC302-TeamRocket

[![Docker-CI](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/docker-ci.yml)
[![Pylint](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/lint.yml/badge.svg)](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/lint.yml)
[![Python application](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/python-ci.yml/badge.svg)](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/python-ci.yml)
[![Node.js CI](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/nodejs.yml/badge.svg)](https://github.com/menghaoyu2002/CSC302-TeamRocket/actions/workflows/nodejs.yml)

## Project Overview

This project is a tool to visualize data from a particular dataset by using a simple web interface. The overall goal for the project is to present the dataset in a way that is easy to digest so that it sparks interest and quetions into the dataset. The particular dataset we have chosen contains data on the percentages of various populations that are considered undernourished, or do not meet the minimum caloric intake defined as necessary for a given population. We presented our data through graphs in a way that you can compare the undernourishments of various populations over time. We believe this makes it easy for anyone to see the vast differences in undernourishment between populations and their changes over time. This subject matters to us because undernourishment is still a real problem throughout the world. The UN has set a Sustainable Development Goal to end hunger by 2030 but we are still far from this goal. Our team wishes to shed light on this issue and spark interest in others too.

## Documentation

Documentation can be found in our [Github Wiki](https://github.com/menghaoyu2002/CSC302-TeamRocket/wiki)

## Meeting Notes

Meeting notes and postmortems can be found in our [meeting-notes folder](https://github.com/menghaoyu2002/CSC302-TeamRocket/tree/main/meeting-notes)

## Roadmap

The roadmap can be found in the the [root directory](https://github.com/menghaoyu2002/CSC302-TeamRocket) of our repo in a file named [ROADMAP.md](https://github.com/menghaoyu2002/CSC302-TeamRocket/blob/main/ROADMAP.md)

## Setup

This setup assumes that you are in the root directory of our project, and will break if you are not.

NOTE: it is highly recommended that you run each of our shell scripts as follows where script.sh is the name of the script.

```bash
sudo ./scripts/script.sh
```

For the sake of making the process of running each script a single command we have reduced it to one command. We also chose to omit the sudo command since it would be another dependency for us to manage.

Also note that our setup currently only supports Ubuntu, Debian, Fedora, CentOS. And only supports the package managers apt, dnf, and yum.

We chose to only support these OS because docker is only supported (without binaries) on CentOS, Debian, Fedora, Ubuntu, SLES, and RHEL. For the sake of supporting a more modern and commonly used linux, we chose to omit SLES and RHEL. Although the same setup works with Debian and Ubuntu derivatives, it seemed infeasible to manage such a large number of distros. We've handled this case via referring the user to the manual install page.

If your machine is running something else, you should get an informative error message telling you to install manually.

We have not handled the case where shell scripts cannot be run on the machine, i.e. sh is not available. This seemed like a unlikely situation seeing as that the machine could be assumed to be running a modern linux.

### **Why is admin permissions required?**

We need elevated permissions in order to install docker onto your machine. There is no way around it.

Futhermore, when docker is installed, elevated permissions are required to run any docker command. This is because the user is not yet added to the docker group, which would require another step, and even when automated, will still require the user to logout or restart the machine.

### **Installing Dependencies**

NOTE: only run one of the commands, not both.

This script installs docker and all our dependencies.

```bash
su -c './scripts/install.sh'

# the recommended way if sudo is installed
sudo ./scripts/install.sh
```

### **Building the Application**

This script builds our docker image.

```bash
su -c 'docker compose build'

# the recommended way if sudo is installed
sudo docker compose build
```

### **Running the Application**

This script runs our docker container, i.e. the application.

```bash
su -c './scripts/run.sh'

# the recommended way if sudo is installed
sudo ./scripts/run.sh
```

Then navigate to http://localhost:3000 to view the running application.

### **Running Tests**

This script runs all our tests. NOTE: the application must be first built before tests can be run.

```bash
su -c './scripts/test.sh'

# the recommended way if sudo is installed
sudo ./scripts/test.sh
```

# Validation, Verification, and Acceptance Criteria

## Acceptance Criteria

Our acceptance creteria is defined under each milestone [here](https://github.com/menghaoyu2002/CSC302-TeamRocket/blob/main/ROADMAP.md).

## Validation and Verification

#### Milestone 1: Set up repository, dev environments, and initial files. Project can build, run and connect to the database.

The acceptance criteria was validated through unit tests in the backend with pytest. It was continuously validated with our Github Actions CI/CD pipeline, which runs these unit tests and verfies if the build is successfully on every change to the codebase.

Checking whether or not our program can be installed, built, run, and tested on a linux machine was validated manually before every deliverable.

#### Milestone 2: Able to import data into the database on server and get data with a basic interface.

All database criteria was verified with unit tests in the backend. Data fetching with a basic interface was verified with unit tests and manually validated through running and interacting with the application. These new unit tests are ran on every change to continuously validate that our applicatoin is working as we intended it to.

#### Milestone 3: Able to perform transformations/calculations on the data and display them upon user request with a simple web-page.

All backend transformatoins and calculations on the data were verified with unit tests in the backend. Each transformation is a tested endpoint in our backend. The rendering of the web page was unit tested with jest and verified manually. All unit tests once again were run by our CI/CD and validated with manual testing.

#### Milestone 4: Make the web-page interactive, allowing the user to see data transformations as they adjust values on the page.

Starting from milestone 4, all user interaction tests were simulated with an end to end testing framework (cypress). This means that the usability of our application was continously verfied by end to end tests instead of manually. These tests verify that our web page is in fact interative, that it does in fact retrieve the data, and that the data is displayed in a visual manner, and thus have validating that we have met the acceptance criteria of the milestone. These tests were integrated with our CI/CD pipeline.

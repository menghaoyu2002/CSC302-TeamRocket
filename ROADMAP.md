# Road Map

## What?
We want to build an web application that can import a dataset about undernourishment in different parts of the world, store the relevant information in a database, then dispay the data to the user. We will accomplish this in 4 milestones:  

1. Set up repository, dev environments, and initial files. Project can build, run and connect to the database. (complete)
2. Able to import data into the database on server and get data with a basic interface. (~2 weeks)
3. Able to perform transformations/calculations on the data and display them upon user request with a simple web-page. (~3 weeks)
4. Make the web-page interactive, allowing the user to see data transformations as they adjust values on the page. (~2 weeks)

## How?
For milestone 1, we had:  
 - Jeremiah set up the initial back end and work on some documentation and road map write up.
 - Michael set up initial tests and write documentation.
 - Menghao set up initial environment and install/build/run scripts  

For milestone 2, we had:  
 - Jeremiah implement CI/CD workflows/frameworks
 - Michael develop backend data processing
 - Menghao work on tests and front end design/implementation  

For milestone 3, we will have:  
 - Jeremiah work on data transformations + CI/CD
 - Michael develop web-page UI
 - Menghao develop tests and help develop back end  

For milestone 4, we will have:  
 - Jeremiah creating end to end tests
 - Michael develop interactive UI
 - Menghao develop interactive UI

## Features
In order of higheset priority, future features are described below:  

The next features we intend to implement is the ability to visualize our data using graphs. We want to be able to plot the undernourishment in a given country vs time as a plot/line graph. This is the highest on our priority list because in the project's current state, we are displaying a list of data which is very hard to read, let alone interpret the meaning behind the data. Since we thought a visual representation such as a graph would make interpreting the data much easier and more pleasant, this would be our next goal to make the application more meaningful. Moreover, it will not be too difficult since we have the endpoints ready for it.  
What needs to be done?:  
- Investigation on whether we should create/use a graph UI component or display images of graphs using something like plotly. (By Jeremiah due next meeting Nov 6)
- Creation of reusable component for graph (By Michael due Nov 9)
- Integrate component into the page (By Menghao due Nov 12)  

Acceptance Criteria:
- User can see at least 1 graph of undernourishment over time by inputing a country name.

Another feature we would like to have is the ability to aggregate the data for a category and display the average in a visually appealing way. Ideally we would like a pie chart to show how many people in the given population on average are undernourished. We believe this is a nice way to generalize our findings for a given country which is important but it was not as impactful as our graph since the average does not capture all the details of the data.

What needs to be done?:
- Creating a component to display the average (Jeremiah by Nov 15)
- Integrage the component into the page (Michael by Nov 18)
- Create UI tests for the components that have been created (Menghao by Nov 20)

Acceptance Criteria:
- User can choose a country name and see the average undernourishment in a visual way (ideally pie chart but willing to settle for something simpler like a % bar).

A stretch goal that we have is to add the data of multiple countries to the same graph in order to compare their undernourishment values. The reason this feature is prioritized rather low is because there has been no investigation done yet to see if this feature is even possible with our current graphing library, and thus the difficulty of this feature cannot be gauged yet. It is also not crucial for the completion of the MVP for this project, it is just a very nice feature that will make it easier for users to compare and draw meaningful conclusions from our data.

What needs to be done?:
- Investigate whether or not it's possible to plot multiple lines on the same graph with our chosen library (Jeremiah by Nov. 25)
- Create component to add more lines in the graph (Menghao by Nov. 30)
- Create UI tests for the components that have been created (Menghao Nov. 30)
- Integrate component into the page 

Acceptance Criteria:
- User can add muliple countries onto the same graph
- Multiple lines are displayed on the same graph.
- Each line is a different colour representing a distinct country.
- A legend to indicate the country that each colour corresponds to.

This last feature is one that we doubt we will get to, and for this reason, there will not be any dates and estimations regarding workflow. If we have enough time to do this feature then we will come back and reassess it. This last feature is adding linear regression to graphs. The reason this feature has the least priority is because the amount of estimated time and effort it may take to implement this feature. First off, we would have to research how to add linear regression to our project and figure out what libraries to use, and be intentful with the decisions we make. Second off, background knowledge in linear regression might even be required in order to use the library and generate an accurate line of best fit; this would have to be investigated. Lastly, we would have to build this feature from the ground up, we have no existing infrastructure to build on top of. This reason is the reason why this feature is ranked as the lowest priority, because building new features from the ground up is expensive in terms of time and effort. If we choose to do this feature, we may not be able to get to other features that are more crucial to our MVP. Linear regression is not a necessity, and the workload would require us to put off other features that *are* necessities. For this reason, this feature will only be implemented once everything else is done. There are still too many unknowns at this point to even begin trying to guage which tasks are needed in order to complete this feature. Extensive investigation is required.

## Milestone Progress

Since Assignment 1 we have demonstrated progress as we completed milestone 2. So the next milestone we are progressing towards is milestone 3.  

Success for this milestone means creating a simple web page so that we can display our data and perform basic data transformations. We want the web page to be easy to use and easy to interpret data through visualizations. Moreover, we want the user to be able input some fields so that we can display our data in multiple ways that are all meaningful. For example, the user should be able to request and get data over time, averages, linear regressions, and specific queries for certain dates and date ranges. In addition, our web page should have easy access (launchable/accessible in one step).  

Responsibilities for each team member for this milestone are:  

Jeremiah:
 - Create 1 - 2 server endpoints (Completed)
 - Create initial interface regardless of UX (Completed)
 - Visualize average data using a pie/bar chart (To do)
 - Create unit tests for these features (To do)
 - Integrate multi line graph feature into the app (To do?)

Michael:
- Create 1 - 2 server endpoints (99% In progress)
- Improve the UI/UX to be reasonably pleasing (In progress)
- Visualize data using graphs (To do)
- Create unit tests for these features (To do)
- Add tests for multi line graph components (To do?)

Menghao:
 - Create 1 - 2 server endpoints (Completed)
 - Set up front end subproject (Completed)
 - Set up docker containers for both front end and back end so that they can be run together (Completed)
 - Integrate new components into app (To do)
 - Create e2e/integration tests for the features (To do)
 - Create multi line graph components (To do?)

Validation process:
- At least 1 graph representing undernourishment over time.
- The user has a way to filter this graph data by a date range.
- One way to visualize average undernourishment for each population.
- If above is completed in 2 weeks, a way for a user to see lines for multiple populations on one graph

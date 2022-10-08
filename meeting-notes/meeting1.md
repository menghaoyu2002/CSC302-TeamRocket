# Summary of the meeting

The team met on October 3rd to discuss the following:

- How and when meetings are held.

- What product we will deliver along with a potential dataset to use
  as well as key milestones to measure progress.

- Our choice of tech stack and why after taking into consideration the
  experience of each team member, as well as advantages the tech stack
  provides.

- Deciding on which tasks were to be divided and worked on for
  assignment 1 submission.

# How meetings are held and when

- Our team decided on hosting weekly online meetings on Sunday at 2pm
  EST using discord.
- We practice what we were taught in class, such as having and cycling
  through different notetakers each week, as well as potentially
  having a ticket system for talking. (Limit number of people speaking
  up during meeting.)
- The first meeting using this plan will be on Sunday, October 9th
  2022 at 2:00pm EST. **Notetaker: Jeremiah**.

# Our main deliverable

- Our choice for project is a web app.

- This web app will be an interactive website built using react that
  allows users to display and manipulate our chosen dataset, stored in
  a python + sqlite backend.

# Brief Summary of Milestones

- Build project, connect to sqlite database, display data on screen.

- Import data into sqlite and be able to read and write data using a
  command line interface.

- Allow transformations on data and display graphs + data onto
  website.

- Make webpage interactive and add endpoint tests.

  - Two options

     1\. A cli app that can display graphs and visualize data when required.

       \$ tool -display from jan 1 feb 2 -\> shows graph/data
       \> in browser

     2\. A web application that is interactable, this will be the main interface that the user interacts with. This abstracts away the need to use cli flags and pass
    arguments.

       We chose the web application because of its ease of use.
       It abstracts many of the details away, with buttons
       and visual interfaces.

# Reasons why we chose our tech stack

## Why react?

- We wanted the ability to create a high-quality interactive webpage
  that interacts with a database. React is a popular choice for these
  types of applications.
- React is one of the industry standards for creating high-quality
  websites with javascript + CSS with lots of well-written
  documentation and resources.
- Everyone in our group has some experience using react for web
  development.

## Why Python + SQLite?

- Python is very easy to work with data

- Many Python libraries are focused on data analysis andtransformation

- https://github.com/simonw/datasette built with python + sqlite

- Python has lot of data analysis libraries, pandas, sci-kit learn

- Common for scripting

- Python has poor performance compared to other languages

  - Performance not a big concern

- Dynamically typed :(

  - We may run into errors where the wrong type is passed into a
    method.

  - These errors would be caught in typed and compiled languages,
    but python is none of those things

  - One solution is that we can use some built in type annotations
    to help aid this issue in clarification, but python does not
    technically enforce this.

## Why Javascript?

- Classic for web dev, especially with react.

- One language for both frontend and backend.

## What else did we consider?

### R Language

- R has seamless integration with many data science packages.

- Some packages are better for displaying/visualizing data

- R is generally better at doing statistics than python

- However, since the team is mostly inexperienced with using R, we
  chose to not use R in the end.

### Java/Kotlin + SQLite

- Classic combination for many android applications.

- Does not necessary have an advantage over python for data analysis.

- Potential datasets: covid/virus stats, nutritional info

- What to build

  - Import dataset, convert to sqlite, display with interactive webpage

  - Milestones

- Go + SQLite

  - [[https://github.com/mergestat/mergestat-lite]{.underline}](https://github.com/mergestat/mergestat-lite)

  - [[https://github.com/benbjohnson/litestream]{.underline}](https://github.com/benbjohnson/litestream)

  - Not exceptionally good at working with data and analyzing data.

- Containers

  - Only experience with docker and make/cmake

  - Docker commonly used

  - We will use docker because it will simply some assumptions we need to make about the user's machine

   - We don't need to assume it has ANY of our dependencies on it except docker

    - Instead, we will make all our assumptions about the docker container instead

    - What this means is, although we can't assume that python isinstalled on the user's machine, we can and will assume that python will be installed in our container.

    - Since we get to choose which OS our docker image uses, we do not need to worry about what package manager is installed on the user's machine

     - We  _know_ exactly what package manager is installed on our docker image

  - We also considered using make to allow the user to run the build, test, run commands via make.

   - After some consideration, it seems like make will just be another dependency that we do not know is on the user's machine or not

    - If it isn't we would have to install it

    - How do we install it?

     - We could automate this but we would need to know
          what the package manager is on the user's machine

    - Instead, we will just settle and use bash scripts instead.

     - Although bash scripts don't track dependencies and therefore can be run unnecessarily, this trade off seemed okay (why?)

     - We are using python, which is not a compiled language. This means we do not need to compile anything with make, and thus the dependency management is redundant to us.

     - Although the build script may build an identical docker image at times, this is a tradeoff we are willing to make.

     - This does not cause anything to break

     - However, it does cause time and resources to be wasted building a duplicate image.

     - Docker does cache builds (i think).

     - This might be an issue we need to address in the future if it's a big enough problem.

     - It is always easy to convert back to make
              files when we already have bash scripts
              that build, test, and run.

- Why SQLite?

  - Small, very easy to set up, has built in integration with python.

  - Local! If someone else changes their database, we should not need to update any others! Databases are local and do not need to be synchronized

  - Can store lots of data if needed.

  - For scope of project, we don't need a large server for database

  - [[https://www.sqlite.org/whentouse.html]{.underline}](https://www.sqlite.org/whentouse.html)

- Frontend visualization

  - 3 big choices: React, Angular, Vue

   - All do the same thing, not super different from each other.

  - For our purpose, Angular might have too much overhead.

   - Our scope is smaller, no need to use a full on framework!

  - Which one has the best support for visualization data?

   - Do we even need to use a front end framework?

    - Which one has the best support for displaying graphs?

     - React

     - [[https://canvasjs.com/react-charts/]{.underline}](https://canvasjs.com/react-charts/)

     - [[https://github.com/recharts/recharts]{.underline}](https://github.com/recharts/recharts)

     - [[https://uber.github.io/react-vis/]{.underline}](https://uber.github.io/react-vis/) (deprecated)

     - Vue

     - [[https://vue-chartjs.org/guide]{.underline}](https://vue-chartjs.org/guide)

    - Maybe We don't even need a frontend framework?

     - Python can display graphs with this!
        [[https://plotly.com/]{.underline}](https://plotly.com/)

  - Pytest will be used for testing

   - All testing will be done with Pytest because all unit testing frameworks are more or less the same. Our team is most familiar with pytest.

   - It is a unit testing framework. We do not necessarily have to do automation tests/end to end just yet.

# Immediate Next steps

- At the bare minimum we need to (in order)

  - Connect an empty sqlite db to our python backend (Jeremiah)

   - Print('Yay sqlite has been connected')

  - Create test files that simply print "tests are running" \*\*for now (Michael)\*\*

  - Create a command line script that can run _all_ our tests. (Menghao)

  - Create command line script that can build our application (Menghao)

   - That is, it will create a container that has a running
      instance of our python application within it.

  - Create a documentation/wiki page that tells the user how to
    build, run, and test our application. (Everyone)

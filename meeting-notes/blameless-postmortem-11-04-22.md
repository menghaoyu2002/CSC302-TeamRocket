# Blameless Postmortem
#### 11/04/2022

## Goals Achieved
- Selected a dataset meaningful to us (undernourishment in various populations in the world)
- Import dataset into database and create methods to access the data
- Created some endpoints to access and filter the data for a client to use
- Created a simple web interface to access and view the data by inputing request data into some fields (Milestone 2)
- Implement simple CI/CD using github actions to help enfore the one way quality ratchet

## Goals Missed
- We set out 4 endpoints to create by the end of this week but due to some unforseen circumstances, only 3 were completed.
- We also planned to make our basic interface at least slightly aesthetically pleasing by the end of this week, but we didn't account for midterms and other workloads so this goal was missed (the webpage has virtually no styling, only html).
  - This goal was not missed by that much since the page was only temporary, and any styling added would've likely been removed since the page would be reformatted into graphs
- while not necessarily a goal missed, an issue that needed to be addressed is how big changes into the codebase can be merged without breaking branches that others are working on.

## Plan Adjustments
- Based on the time we have left, we may have to scratch the idea of having more sophisticated data transformations like linear regressions.
- We noticed we made and merged PRs at a slower pace than expected which really puts a damper on the rate at which we progress. Moreover, we noticed we tend to do tasks more or less one after the other no matter who is working on it. One adjustment could be to divide tasks in such a way that we can work on them at the same time without having to wait on others to finish.
- We should also break PRs down into smaller chunks so we do not have to wait for a large code change to be created, reviewed, and merged. Hopefully this will improve the rate at which we improve the application.
- We also learned that when working together and making sure each code change is robust and mitigates/avoids failure, our ideas cannot be turned into code as fast as we thought as it takes planning, coding, reviewing, and testing which takes longer than just writing code nonstop for a toy project. In light of this, we should lower our expectations for having interesting interactive features for milestone 4 like the idea to extrapolate/predict data as the user adjust sliders and modifies data.
- In terms of our missed goals, we realized that we could not allocate as much time as we thought into this course as most of us were extremely busy with other midterms and projects which is why we missed 2 of our goals for this week. This is also a reason why we should reduce our scope a bit and lower the expectations for our weekly tasks by making our PRs/tasks smaller.
- Estimations should be given for each task, by the person assigned to each task.
  - this estimation must reflect all factors that may affect the completion of the task
  - this includes, course work, fatigue, any external circumstances as well.
- If assisstance is required, the team should be informed early.
- Big changes should be announced first to the team, this can avoid merge conflicts
- Big changes should be broken down into smaller changes
- Be aware of what changes you're making, if you know a portion of your change affects others, get that part merged in first

# Hats4Cats


### Tasking Instructions
Below is a lit of stuff for us to do. Overall category of the task is first, name of the task is second, description of the task is third.  
If you are actively working on a task, please edit this document and put your name in parenthesis next to the task so we don't step on your toes.  
Please only checkout a maximum of two tasks at a time.  
If a task is done, please write (DONE) next to the task.  

### Tasking

Design - Draw Hats - Need at least either three hats of different orientation (left, front, right) or three different hats one of each of those orientations. (DONE)
  
Design - Design UX/UI - How is the user uploading a picture? What will the "look" look like?

Frontend - Javascript - Build app for uploading photo
  * Should user be able to select hat?

Cloud - Design backend -> Cloud Services:
  * How to create secure S3 bucket?
  * How to move photo to S3 bucket?
  * How to trigger an event on photo upload?
  * How do you track the photo through the pipeline so the user receives the correct photo back?

Backend - Python - Design backend:
  * How to import picture of hat?
  * How to import picture of cat?
  * How to detect eyes, nose, and ears? (Might need to leverage AWS machine vision)
  * How to find hat placement midpoint on X-Y axis using facial geometry?
  * How to use hat metadata (midpoint, size, rotation) to place hat on X-Y axis?
  * How to use facial geometry to calculate tilt necessary for hat placement?
  * How to use hat metadata to rotate hat around midpoint?
  * How to export flattened photo?

Meta - Code repo - Where are we storing everything? (DONE)  
Meta - Liveshare - How are we pair-programming (if at all?)  
Meta - Tasking - How are we displaying this document? (DONE)  

# Crossmint Challenge

The challenge of this exercise is to interact with API created by Crossmint 
to create special diagram that Crossmint refers to "your own megaverse".

## Design Approach Rationale

One of the core parts of the challenge is the ability to make HTTP request calls for 
different types of astral objects such as polyanet, soloon, and comeths. 

My approach created one parent class (APIHelper) that contained methods that were 
related to HTTP GET and HTTP POST. Next, I created subclasses for each of the different 
types of astral objects so that there was a better abstration of logic. 

Additionally, I also created one class (MatrixUtils) which contained methods related
to processing the raw Matrix string. While it was easy to split the input such as 
DOWN_COMETH and making the string lowercase, I felt that the code would be a lot cleaner
if all of these combinations were inside a dict. 

Overall, by placing each of the classes for the astral objects into a seperate class, I 
was able to avoid the common logic paradigm of a series of if conditions that often 
make methods very bloated and difficult to read. 

## Unit Test

In this particular challenge, I also created a unit test file for the HTTP request logic
which is where errors can occur. 

## Conclusion 

Thank you so much for giving me the opportunity to work on this exercise and hopefully,
this work demonstrates some of the skills that I can bring to the role if I am selected to 
move forward in the interview process. 
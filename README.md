

# Run instruction

The solution was programmed with Python 3.6.2. In the 'run.sh' I still use python and it worked. 

The running of the solution requires no additional library, environment, or dependency. Only the Python Standard Library is used.

The code was tested on a computer with Windows Subsystem for Linux (Ubuntu 16.04.2 LTS). The two bash files 'run.sh' and 'run tests.sh' worked well on the test1 coming with the challenge and also my own test2 as shown in the folder. I also tested the large dataset containing over 24 million records over [here](https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view), it worked but I didn't have a way to validate the result for such a large file.

![](http://https://drive.google.com/file/d/1JwA3h2CSGU3OQ-I93VlV_vnwUo7I29IG/view)


# Approach

For this challenge, I employed a 'cost' dictionary to record the total cost of a single drug, and another 'prescriber' dictionary to record all the unique prescribers for the drug. The dict key for the all two dictionaries are the name of the drug, and I use the combination of the last name and first name for identification of each unique prescriber. The steps of the solution are as below:

1. Streaming each line from input file.

2. Identify and name all the useful fields from each line, and validate those input items in the right format, specifically, the 'id' should be in int format and cost should be in float format. This part was done by the codes in helper.py.

3. Go through the input file and record all the drugs and their total costs as well as the unique prescribers. The prescribers were recorded in a set in the dictionary data to make sure they are unique.
 
4. Sort the drugs in descending order based on the total drug cost and if there is a tie, drug name. Write the sorted drug information to the output file.
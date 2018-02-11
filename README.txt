CS 6350 - Spring 2018
HW1 - Decision Tree
Taylor Welker
u0778812

To run:  Simply run the file 'run.sh'.  It is preset to pass in train.csv, test.csv, and return the required data for problem 3 in 'output.csv'.  Please don't move these files as they are hard coded into the main.py file.  If the grader wishes to move these files, they will have to update the call to main() at the bottom of main.py with the correct file paths.

The output is located in output.csv.  If you wish to view the data in a table, simply open the file with some Excel Spreadsheet application.

Note: This data includes decision tree errors for every depth specified (1-7) as well as for every heuristic used to separate the nodes (info gain vs majority error).

Files:

--Python Files--
Attributes.py:  Used to help keep track of the values each attribute can take
Dataset.py: Used to create Datasets that take information from the input files and send them to a DecisionTree object to get parsed and used.
DecisionTree: Where the ID3 magic happens
Example.py: Class object to hold instances of examples within the given dataset.
Leaf.py: A leaf node object.  Simply holds a label within the tree.
main.py: Call this to run the program.  To modify the program's inputs, simply modify the call to 'main()' at the bottom of this file.
Node.py: Nodes are used to help organize the tree.  These hold their children (Nodes and Leaves), as well as the index of the attribute they split on.
UtilityFunctions.py: This holds functions used for calculating the Information Gain, Majority Error, as well as other useful functions for the DecisionTree to use.

--Data Files--
*inputs
data-desc.txt: as described in the project description
train.csv: as described in the project description
test.csv: as described in the project description
dt_data.xls: the dataset from Section 1 of the homework.  Used for initial testing of Information Gain, Majority Error, and Decision Tree functions.  To use, you must modify the call to main() by replacing 'csv' with 'xls', and put this file as both the training and test input files.
shape_color.xls: the dataset that consists of colored shapes from the lectures.  Used for initial testing of information gain, majority error, and decision tree functions.  To use, you must modify the call to main() by replacing 'csv' with 'xls', and put this file as both the training and test input files.

*outputs
output.csv - where the data from running main.py goes

This data was tested on the datasets found in section 1 of the homework as well as the colored shapes dataset from the slides.  After making the trees by hand (testing the info gain on each of them, and the majority error on the first), I believe that they are working as intended.  Therefore, I am fairly confident that the error values being returned from the train.csv and test.csv files are accurate.

However, don't try to use the 'printTree' function...it doesn't work as I intended it to.  Simply use the data as provided.  If you wish to examine the tree structure, you will have to use a debugging tool and look at the children of the root node, and their children, and so on and so forth.

ALSO...apparently the CADE machines don't support import xldr.  So simply ignore any files having to do with .xls, and don't uncomment anything...I had to manually remove the additional functionality that my program provided in order to please the CADE overlords...if you can't tell, I was pretty frustrated with this...stupid CADE machines...

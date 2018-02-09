import xlrd
from Example import Example
from Dataset import Dataset
from DecisionTree import DecisionTree

# This function simply tests whether or not we can find the most common label in a set of examples
def testMostCommonLabel(dataset):
    newDT = DecisionTree(1)
    label = newDT.getMostCommonLabel(dataset.getExampleList())
    print "This is the most common label in the dataset: ", label

def main(filename):
    dataset = Dataset(filename)
    dataset.parseDatasheet()
    testMostCommonLabel(dataset)
    print("Done")


main('dt_data.xls')
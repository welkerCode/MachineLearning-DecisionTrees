import csv
import xlrd
from Example import Example
from Dataset import Dataset
from DecisionTree import DecisionTree
from UtilityFunctions import *

# This function simply tests whether or not we can find the most common label in a set of examples
def testMostCommonLabel(dataset):
    newDT = DecisionTree(1)
    label = newDT.getMostCommonLabel(dataset.getExampleList())
    print "This is the most common label in the dataset: ", label

def main(training_filename, test_filename, output_file, data_type):
    allDepthErrors = {}
    for x in range(1, 8):
        listOfErrors = testTreeDepth(training_filename, test_filename, x, data_type)
        listOfErrors.append((listOfErrors[0] + listOfErrors[2])/2) # averageTrainingErr
        listOfErrors.append((listOfErrors[1] + listOfErrors[3])/2) # averageTestingErr
        listOfErrors.append((listOfErrors[0] + listOfErrors[1])/2) # averageInfoGainErr
        listOfErrors.append((listOfErrors[2] + listOfErrors[3])/2) # averageMajorityErr
        listOfErrors.append((listOfErrors[0] + listOfErrors[1] + listOfErrors[2] + listOfErrors[3]) / 4)  # averageTreeDepthError
        listOfErrors.insert(0,x)
        allDepthErrors[x] = listOfErrors

    dataLabels = ["Tree Depth", "Info Gain Training Err", "Info Gain Testing Err", "Majority Error Training Err", "Majority Error Testing Err", "Average Training Err", "Average Testing Err", "Average Info Gain Err", "Average Majority Error Err", "Average Tree Depth Err"]

    with open(output_file, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(dataLabels)
        for iteration in allDepthErrors:
            row = allDepthErrors[iteration]
            writer.writerow(row)
    print "Done.  See the results in 'output.csv'..."

def testTreeDepth(training_filename, test_filename, max_depth, data_type):
    # Create datasets for the training and testing files
    trainingDataset = Dataset(training_filename)
    testingDataset = Dataset(test_filename)

    # Parse the data according to the type specified by 'data_type'
    if data_type == 'xls':
        trainingDataset.parseDatasheet()
        testingDataset.parseDatasheet()

    else:
        trainingDataset.parseCSV()
        testingDataset.parseCSV()

    # Additional Setup
    trainingDataset.createAttributeList()
    testingDataset.createAttributeList()

    # Finally, create the Decision Trees (one for each algorithm) specified by max_depth
    DT_info = DecisionTree(max_depth, trainingDataset.getAttributeList())
    DT_majority = DecisionTree(max_depth, trainingDataset.getAttributeList())
    DT_info.buildTree(trainingDataset.getExampleList(), 'info')
    DT_majority.buildTree(trainingDataset.getExampleList(), 'majority')

    '''
    Here, we calculate the following errors at this depth:
    Training Error: Info
    Training Error: Majority
    Testing Error: Info
    Testing Error: Majoirty
    '''

    errorValues = []
    errorValues.append(getError(DT_info,trainingDataset))
    errorValues.append(getError(DT_info, testingDataset))
    errorValues.append(getError(DT_majority,trainingDataset))
    errorValues.append(getError(DT_majority,testingDataset))

    return errorValues

    #print getInfoGains(dataset.getExampleList())
    #print("Done")

def getError(tree, dataset):
    totalTrials = len(dataset.getExampleList())
    numIncorrect = 0
    for example in dataset.getExampleList():
        correctPred = example.getLabel()
        treePred = tree.predict(example.getAttributes())

        if correctPred != treePred:
            numIncorrect += 1

    return float(numIncorrect)/float(totalTrials)

#main('dt_data.xls')
#main('shape_color.xls', 'shape_color.xls', 'xls')
main('train.csv','test.csv','output.csv','csv')
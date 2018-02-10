import numpy as np

from Example import Example

def calcInformationGain(s, a):
    '''

    :param s: set of examples
    :param a: attribute
    :return: information gain
    '''

    # Gain = Entropy(S) - sum((|Sv|/|S|)*Entropy(Sv))
    # Sv is the subset of examples weher the value of attribute A is set to value v


def calcEntropy(s, specifiedAttribute):

    print None
# Entropy(S) = H(S) = -p+log(p+) - p- log(p-)
# The entropy of an attribute is the sum of the entropy of each of its labels multiplied by the probability of getting that attribute in the first place

# Iterate through the set of examples, getting all the potential values for that attribute and the count for each one in the set
# Also, be sure to get the total number of examples so that we can get our probability
# For each Attribute value in our map:
# Calculate its Hs and store it in a list
# Sum the elements of the list to get the expected entropy.
# Get Hs for the label



# Using numpy.log2
def getHs(probSet):
    Hs = 0
    for probability in probSet:
        Hs = Hs - (probability) * np.log2(probability)
    print Hs
    return Hs

def getLabelTypeCountDict(s):
    labelDict = {}
    for example in s:
        label = example.getLabel()
        if label in labelDict:
            labelDict[label] += 1
        else:
            labelDict[label] = 1
    return labelDict
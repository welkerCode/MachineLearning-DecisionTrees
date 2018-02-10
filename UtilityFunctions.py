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
    return Hs

# This function returns a dictionary of the form: {attribute_value : count}
def getTypeCountDict(s, attributeIndex):
    
    # This is the dictionary that we will return
    attributeDict = {}
    
    if attributeIndex == 'label':
        
        # For every example, get its label.  If it is in the dictionary, increase its count, otherwise add it as a new key
        for example in s:
            label = example.getLabel()
            if label in attributeDict:
                attributeDict[label] += 1
            else:
                attributeDict[label] = 1
        return attributeDict

    else:
        # For every example, get its label.  If it is in the dictionary, increase its count, otherwise add it as a new key
        for example in s:
            attribute = example.getAttributeValue(attributeIndex)
            if attribute in attributeDict:
                attributeDict[attribute] += 1
            else:
                attributeDict[attribute] = 1
        return attributeDict
        

# Get the probability of each label value given an example set s
def getLabelProbabilities(s):

    # I learned to cast ints to floats using float() from www.pitt.edu/~naraehan/python2/data_types_conversion.html

    # Get a dictionary that returns all the possible labels, and their probability given an example set s
    attrDict = getTypeCountDict(s, 'label')

    # This is the list that will hold the probabilities that we will return
    probabilities = []

    # Calculate the probability of each label
    for entry in attrDict:
        probabilities.append(float(attrDict[entry]) / float(len(s)))

    # Return the probabilities
    return probabilities


# This returns a dictionary relating labels to the number of times they occur in relation to a particular attribute value.
def getAttributeLabelCountDict(s, attributeIndex, attributeValue):

    # First, get the proper subset of s
    subset = getExampleSubset(s, attributeIndex, attributeValue)

    # Now, get the dictionary mapping the label types to the number of times they appear in the subset
    return getTypeCountDict(subset, 'label')


# This returns a subset of s corresponding to a certain attribute value
def getExampleSubset(s, attributeIndex, attributeValue):
    exampleSubset = []

    # For every example in the example set s
    for example in s:
        # If the example's attribute matches the value we are looking for, add it to the subset
        if example.getAttributeValue(attributeIndex) == attributeValue:
            exampleSubset.append(example)

    return exampleSubset


def getInfoGains(s):
    labelProbs = getLabelProbabilities(s)
    labelEntropy = getHs(labelProbs)

    informationGains = []

    for x in range(0, s[0].getNumAttributes()):
        # Get the dictionary associating the current attribute with its labels
        attributeValueDict = getTypeCountDict(s, x)

        attrValEntropies = []  # This holds the entropy for each value of a particular attribute
        attributeProbabilities = []  # This holds probability of getting each attribute value


        for value in attributeValueDict:
            attributeProbabilities.append(float(attributeValueDict[value]) / float(len(s)))
            subset = getExampleSubset(s, x, value)
            labelProbs = getLabelProbabilities(subset)
            attrValEntropies.append(getHs(labelProbs))

        expectedEntropy = 0
        for y in range(0, len(attrValEntropies)):
            expectedEntropy += attrValEntropies[y] * attributeProbabilities[y]

        informationGains.append(labelEntropy - expectedEntropy)

    return informationGains

def getMajoirtyErrors(s):
    # Create a list to hold the true majoirty errors
    majorityErrors = []
    # For each attribute
    for x in range (0, len(s[0].getAttributes())):
        # Get the dictionary between the attribute value and the number of times it appears
        attrValueCountDict = getTypeCountDict(s, x)

        subError = 0

        # For each of these values
        for value in attrValueCountDict:


            # Get the appropriate subset of s
            subset = getExampleSubset(s, x, value)

            # Create a dictionary to hold the label with the count
            subsetDict = getTypeCountDict(subset, 'label')


            majorityQuantity = 0
            totalLabelCount = 0

            # Find the max label value
            for labelVal in subsetDict:
                totalLabelCount += subsetDict[labelVal]
                if majorityQuantity < subsetDict[labelVal]:
                    majorityQuantity = subsetDict[labelVal]

            # Calculate the majority error and store it in the list
            subMajorityError = 1 - float(majorityQuantity)/float(totalLabelCount)
            subError = subError + (subMajorityError * (float(attrValueCountDict[value])/float(len(s))))

        majorityErrors.append(subError)
    # Return the true majority errors
    return majorityErrors

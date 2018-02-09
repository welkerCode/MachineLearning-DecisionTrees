from Example import Example

class DecisionTree():

    def __init__(self, newDepth):
        self.maxDepth = newDepth

    def ID3(self, s, attribute, label):
        '''

        :param s: set of examples
        :param attribute: the set of measured attributes
        :param label: the target attribute (the prediction)
        :return:
        '''

        allLabelsMatch = doAllLabelsMatch(s)
        if allLabelsMatch == True:
            if label is not None:
                return Leaf(label,parent)
            else:
                # Most common label
                mostCommonLabel = self.getMostCommonLabel(s)
                return Leaf(mostCommonLabel, parent)
        else:
            newNode = Node(parent)
            # Find an attribute that best splits the data using information gain

            '''
            1. Create a Root node for tree
            2. A = attribute in Attributes that best splits S
            3. for each possible value v of that A can take:
                1. Add a new tree branch corresponding to A=v
                2. Let Sv be the subset of examples in S with A=v
                3. if Sv is empty:
                    add leaf node with the most common value of Label inS
                   else:
                    below this branch add the subtree ID3(Sv, Attributes -{A}, Label)
                4. Return Root node
            '''
            print "nothing"

    # This function checks to see if all of the labels within the example set match
    def doAllLabelsMatch(self, s):
        matching = True
        origLabel = s[0].getLabel()
        for example in s:
            label = example.getLabel()
            if origLabel != label:
                matching = False
        return matching

    # This function returns the most common lable from the set of examples s
    def getMostCommonLabel(self, s):
        labelDict = {}
        for example in s:
            label = example.getLabel()
            if label in labelDict:
                labelDict[label] += 1
            else:
                labelDict[label] = 1

        maxLabelNum = 0
        for entry in labelDict:
            if labelDict[entry] > maxLabelNum:
                greatestLabel = entry
                maxLabelNum = labelDict[entry]
        return greatestLabel


    def findBestAttribute:

    def calcInformationGain(self,s,a):
        '''

        :param s: set of examples
        :param a: attribute
        :return: information gain
        '''

        # Gain = Entropy(S) - sum((|Sv|/|S|)*Entropy(Sv))
        # Sv is the subset of examples weher the value of attribute A is set to value v

    def calcEntropy(self, s, specifiedAttribute):

        # Entropy(S) = H(S) = -p+log(p+) - p- log(p-)
        # The entropy of an attribute is the sum of the entropy of each of its labels multiplied by the probability of getting that attribute in the first place

        # Iterate through the set of examples, getting all the potential values for that attribute and the count for each one in the set
        # Also, be sure to get the total number of examples so that we can get our probability
        # For each Attribute value in our map:
            # Calculate its Hs and store it in a list
        # Sum the elements of the list to get the expected entropy.
        # Get Hs for the label




    def getHs(self, probSet):
        Hs = 0
        for probability in probSet:
            Hs = Hs - (probability) * log(probability)
        return Hs

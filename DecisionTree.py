from Node import Node
from Leaf import Leaf
from Example import Example
from UtilityFunctions import *

class DecisionTree():

    def __init__(self, newDepth, attributeList):
        self.maxDepth = newDepth
        self.rootNode = Node()
        self.attributeList = attributeList

    def buildTree(self, s, alg):
        self.rootNode = self.ID3(0, s, None, None, alg)

    def ID3(self, depth, s, attribute = None, label = None, alg = 'info'):
        '''

        :param s: set of examples
        :param attribute: the set of measured attributes
        :param label: the target attribute (the prediction)
        :return:
        '''

        if(depth == self.maxDepth):
            return Leaf(self.getMostCommonLabel(s))

        allLabelsMatch = self.doAllLabelsMatch(s)
        if allLabelsMatch == True:
            label = s[0].getLabel()
            if label is not None:
                return Leaf(label)
            else:
                # Most common label
                mostCommonLabel = self.getMostCommonLabel(s)
                return Leaf(mostCommonLabel)
        else:
            newNode = Node()

            # Find an attribute that best splits the data using information gain
            (bestAttributeIndex, __) = self.findBestAttribute(s, alg)
            bestAttribute = self.attributeList[bestAttributeIndex]
            newNode.splittingAttr = bestAttributeIndex
            #attrDict = getTypeCountDict(s,bestAttributeIndex)
            for value in bestAttribute.values:
                #subsets.append(getExampleSubset(s, bestAttributeIndex, value))
                subset = getExampleSubset(s, bestAttributeIndex, value)
                if len(subset) > 0:
                    newNode.children[value] = self.ID3(depth+1,subset,None,None,alg)
                else:
                    mostCommonLabel = self.getMostCommonLabel(s)
                    newNode.children[value] = Leaf(mostCommonLabel)

            #for subset in subsets:
            #    newNode.children.append(self.ID3(subset,None,None,alg))

            return newNode

            # Create a subset for each attribute value for the best attribute

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
        labelDict = getTypeCountDict(s, 'label')

        maxLabelNum = 0
        for entry in labelDict:
            if labelDict[entry] > maxLabelNum:
                greatestLabel = entry
                maxLabelNum = labelDict[entry]
        return greatestLabel


    # This function find the best attribute to split the tree node on and returns the tuple (attr, infoGain)
    def findBestAttribute(self, s, algorithm):
        if algorithm == 'majority':
            majorityErrors = getMajoirtyErrors(s)
            minError = 1
            minAttribute = 0

            for x in range(0, s[0].getNumAttributes()):
                if majorityErrors[x] < minError:
                    minError = majorityErrors[x]
                    minAttribute = x

            return (minAttribute, minError)

        else:
            infoGains = getInfoGains(s)
            maxGain = infoGains[0]
            maxAttribute = 0

            # Loop through the info gains, looking for the maximum value
            for x in range(0, s[0].getNumAttributes()):
                if infoGains[x] > maxGain:
                    maxGain = infoGains[x]
                    maxAttribute = x

            return (maxAttribute, maxGain)


    def predict(self, attributes):
        return self.rootNode.prediction(attributes)

    # Currently doesn't work the way I want yet...
    def printTree(self):
        print self.rootNode.printNode()
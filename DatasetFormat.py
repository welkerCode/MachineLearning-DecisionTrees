class DatasetFormat:

    '''
    Because this Search Tree has to work with a single problem, I thought
    it prudent to simply hard-code in the values specified by 'data-desc.txt',
    rather than to build a parser
    '''


    def __init__(self):
        self.labelValues = [unacc, acc, good, vgood]
        self.attributes = {
            "buying" : ["vhigh", "high", "med", "low"],
            "maint" : ["vhigh", "high", "med", "low"],
            "doors" : ["2", "3", "4", "5more"],
            "persons" : ["2", "4", "more"],
            "lug_boot" : ["small", "med", "big"],
            "safety" : ["low","med", "high"]
        }
        self.attributeOrder = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "label"]

    def getLabelValues(self):
        return self.labelValues

    def getAttributeDictionary(self):
        return self.attributes

    def getAttributeOrder(self):
        return self.attributeOrder
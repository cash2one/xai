

#calss header
class _CORE():
	def __init__(self,): 
		self.name = "CORE"
		self.definitions = [u'most important or most basic: ', u'a value, belief, etc. that is basic and more important than any other: ', u"the most important or largest part of a company's business activities: ", u'the most important parts of a course of study, that all students must learn', u'found in the main part of the body, but not the arms or the legs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

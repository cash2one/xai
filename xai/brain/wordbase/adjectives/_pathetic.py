

#calss header
class _PATHETIC():
	def __init__(self,): 
		self.name = "PATHETIC"
		self.definitions = [u'causing feelings of sadness, sympathy, or sometimes lack of respect, especially because a person or an animal is suffering: ', u'unsuccessful or showing no ability, effort, or bravery, so that people feel no respect : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

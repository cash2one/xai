

#calss header
class _VISCERAL():
	def __init__(self,): 
		self.name = "VISCERAL"
		self.definitions = [u'based on deep feeling and emotional reactions rather than on reason or thought: ', u'relating to the large organs inside the body, including the heart, stomach, lungs, and intestines']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

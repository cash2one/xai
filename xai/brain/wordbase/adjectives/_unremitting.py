

#calss header
class _UNREMITTING():
	def __init__(self,): 
		self.name = "UNREMITTING"
		self.definitions = [u'never stopping, becoming weaker, or failing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

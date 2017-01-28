

#calss header
class _SMELLY():
	def __init__(self,): 
		self.name = "SMELLY"
		self.definitions = [u'having an unpleasant smell: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

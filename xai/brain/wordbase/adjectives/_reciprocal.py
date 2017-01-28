

#calss header
class _RECIPROCAL():
	def __init__(self,): 
		self.name = "RECIPROCAL"
		self.definitions = [u'A reciprocal action or arrangement involves two people or groups of people who behave in the same way or agree to help each other and give each other advantages.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

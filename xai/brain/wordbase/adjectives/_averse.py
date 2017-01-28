

#calss header
class _AVERSE():
	def __init__(self,): 
		self.name = "AVERSE"
		self.definitions = [u'strongly disliking or opposed to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

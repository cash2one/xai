

#calss header
class _SCRATCH():
	def __init__(self,): 
		self.name = "SCRATCH"
		self.definitions = [u'a group of people brought together in a hurry in order to play together on a particular occasion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

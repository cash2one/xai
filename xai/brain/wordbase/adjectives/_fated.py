

#calss header
class _FATED():
	def __init__(self,): 
		self.name = "FATED"
		self.definitions = [u'not able to be avoided because planned by a power that controls events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

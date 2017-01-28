

#calss header
class _RECURSIVE():
	def __init__(self,): 
		self.name = "RECURSIVE"
		self.definitions = [u'involving doing or saying the same thing several times in order to produce a particular result or effect']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

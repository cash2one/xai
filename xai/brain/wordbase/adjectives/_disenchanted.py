

#calss header
class _DISENCHANTED():
	def __init__(self,): 
		self.name = "DISENCHANTED"
		self.definitions = [u'no longer believing in the value of something, especially having learned of the problems with it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

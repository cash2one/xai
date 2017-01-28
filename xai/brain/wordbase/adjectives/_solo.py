

#calss header
class _SOLO():
	def __init__(self,): 
		self.name = "SOLO"
		self.definitions = [u'alone; without other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

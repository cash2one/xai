

#calss header
class _METROPOLITAN():
	def __init__(self,): 
		self.name = "METROPOLITAN"
		self.definitions = [u'relating to a large city: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

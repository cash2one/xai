

#calss header
class _DUSKY():
	def __init__(self,): 
		self.name = "DUSKY"
		self.definitions = [u'dark in colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _HAZARDOUS():
	def __init__(self,): 
		self.name = "HAZARDOUS"
		self.definitions = [u'dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

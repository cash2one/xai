

#calss header
class _PERILOUS():
	def __init__(self,): 
		self.name = "PERILOUS"
		self.definitions = [u'extremely dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

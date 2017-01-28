

#calss header
class _ANAEROBIC():
	def __init__(self,): 
		self.name = "ANAEROBIC"
		self.definitions = [u'not needing or without oxygen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

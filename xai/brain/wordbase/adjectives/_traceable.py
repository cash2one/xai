

#calss header
class _TRACEABLE():
	def __init__(self,): 
		self.name = "TRACEABLE"
		self.definitions = [u'possible to trace: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

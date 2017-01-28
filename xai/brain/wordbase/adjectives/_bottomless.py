

#calss header
class _BOTTOMLESS():
	def __init__(self,): 
		self.name = "BOTTOMLESS"
		self.definitions = [u'without a limit or end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

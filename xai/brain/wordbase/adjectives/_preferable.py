

#calss header
class _PREFERABLE():
	def __init__(self,): 
		self.name = "PREFERABLE"
		self.definitions = [u'better or more suitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

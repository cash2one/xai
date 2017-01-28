

#calss header
class _DEPLETED():
	def __init__(self,): 
		self.name = "DEPLETED"
		self.definitions = [u'reduced: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

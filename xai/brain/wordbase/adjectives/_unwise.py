

#calss header
class _UNWISE():
	def __init__(self,): 
		self.name = "UNWISE"
		self.definitions = [u'stupid and likely to cause problems']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

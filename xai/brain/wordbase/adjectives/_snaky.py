

#calss header
class _SNAKY():
	def __init__(self,): 
		self.name = "SNAKY"
		self.definitions = [u'annoyed or angry']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

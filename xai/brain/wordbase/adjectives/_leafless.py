

#calss header
class _LEAFLESS():
	def __init__(self,): 
		self.name = "LEAFLESS"
		self.definitions = [u'having no leaves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

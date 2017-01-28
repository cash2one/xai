

#calss header
class _PEPPERY():
	def __init__(self,): 
		self.name = "PEPPERY"
		self.definitions = [u'having a spicy flavour like pepper: ', u'easily annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

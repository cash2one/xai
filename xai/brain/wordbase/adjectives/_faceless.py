

#calss header
class _FACELESS():
	def __init__(self,): 
		self.name = "FACELESS"
		self.definitions = [u'having no clear characteristics and therefore not interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

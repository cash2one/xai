

#calss header
class _TUNELESS():
	def __init__(self,): 
		self.name = "TUNELESS"
		self.definitions = [u'having no tune and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

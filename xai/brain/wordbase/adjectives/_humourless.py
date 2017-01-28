

#calss header
class _HUMOURLESS():
	def __init__(self,): 
		self.name = "HUMOURLESS"
		self.definitions = [u'having no humour ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

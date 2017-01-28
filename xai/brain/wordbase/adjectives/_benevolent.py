

#calss header
class _BENEVOLENT():
	def __init__(self,): 
		self.name = "BENEVOLENT"
		self.definitions = [u'kind and helpful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

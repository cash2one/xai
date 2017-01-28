

#calss header
class _EDUCATED():
	def __init__(self,): 
		self.name = "EDUCATED"
		self.definitions = [u'having learned a lot at school or university and having a good level of knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

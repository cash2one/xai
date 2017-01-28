

#calss header
class _POLISHED():
	def __init__(self,): 
		self.name = "POLISHED"
		self.definitions = [u'having been polished: ', u'A polished person has style and confidence: ', u'showing great skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _UNBIASED():
	def __init__(self,): 
		self.name = "UNBIASED"
		self.definitions = [u'able to judge fairly because you are not influenced by your own opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

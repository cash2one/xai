

#calss header
class _SCARY():
	def __init__(self,): 
		self.name = "SCARY"
		self.definitions = [u'frightening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

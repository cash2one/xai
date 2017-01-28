

#calss header
class _FOLKSY():
	def __init__(self,): 
		self.name = "FOLKSY"
		self.definitions = [u'having a traditional, simple artistic or musical style, or pretending to have such a style: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

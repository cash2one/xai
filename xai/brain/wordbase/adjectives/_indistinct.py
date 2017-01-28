

#calss header
class _INDISTINCT():
	def __init__(self,): 
		self.name = "INDISTINCT"
		self.definitions = [u'not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

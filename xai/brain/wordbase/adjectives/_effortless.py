

#calss header
class _EFFORTLESS():
	def __init__(self,): 
		self.name = "EFFORTLESS"
		self.definitions = [u'seeming not to need any effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

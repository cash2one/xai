

#calss header
class _DENSELY():
	def __init__(self,): 
		self.name = "DENSELY"
		self.definitions = [u'with a lot of things close together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

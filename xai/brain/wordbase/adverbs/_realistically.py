

#calss header
class _REALISTICALLY():
	def __init__(self,): 
		self.name = "REALISTICALLY"
		self.definitions = [u'according to the facts and what is possible: ', u'in a way that seems as if it exists: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

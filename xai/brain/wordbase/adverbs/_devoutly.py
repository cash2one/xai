

#calss header
class _DEVOUTLY():
	def __init__(self,): 
		self.name = "DEVOUTLY"
		self.definitions = [u'in a very religious way: ', u'sincerely and strongly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

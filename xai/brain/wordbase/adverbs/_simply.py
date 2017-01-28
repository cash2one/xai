

#calss header
class _SIMPLY():
	def __init__(self,): 
		self.name = "SIMPLY"
		self.definitions = [u'completely or as much as possible: ', u'only: ', u'in an easy way: ', u'in a plain way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

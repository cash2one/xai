

#calss header
class _AS():
	def __init__(self,): 
		self.name = "AS"
		self.definitions = [u'used in comparisons to refer to the degree of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

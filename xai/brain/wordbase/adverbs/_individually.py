

#calss header
class _INDIVIDUALLY():
	def __init__(self,): 
		self.name = "INDIVIDUALLY"
		self.definitions = [u'separately: ', u'in a different and usually original way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

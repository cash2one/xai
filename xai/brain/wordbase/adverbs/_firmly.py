

#calss header
class _FIRMLY():
	def __init__(self,): 
		self.name = "FIRMLY"
		self.definitions = [u'in a way that will not become loose: ', u'strongly and tightly: ', u'forcefully: ', u'in a way that is certain or not likely to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

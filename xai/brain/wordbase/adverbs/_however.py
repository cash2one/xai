

#calss header
class _HOWEVER():
	def __init__(self,): 
		self.name = "HOWEVER"
		self.definitions = [u'despite whatever amount or degree: ', u'used to express surprise: ', u'in whatever way: ', u'despite this: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

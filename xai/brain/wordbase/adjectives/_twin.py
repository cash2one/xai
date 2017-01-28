

#calss header
class _TWIN():
	def __init__(self,): 
		self.name = "TWIN"
		self.definitions = [u'used to describe two similar things that are a pair: ', u'existing at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

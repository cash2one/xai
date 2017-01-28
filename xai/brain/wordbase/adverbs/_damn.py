

#calss header
class _DAMN():
	def __init__(self,): 
		self.name = "DAMN"
		self.definitions = [u'used, especially when you are annoyed, to mean "very": ', u'nothing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

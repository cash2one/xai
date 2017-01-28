

#calss header
class _FARTHER():
	def __init__(self,): 
		self.name = "FARTHER"
		self.definitions = [u'comparative of  far adverb : to a greater distance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

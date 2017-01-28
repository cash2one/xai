

#calss header
class _ALTOGETHER():
	def __init__(self,): 
		self.name = "ALTOGETHER"
		self.definitions = [u'in total: ', u'completely: ', u'considering everything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

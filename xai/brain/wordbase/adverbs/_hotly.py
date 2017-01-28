

#calss header
class _HOTLY():
	def __init__(self,): 
		self.name = "HOTLY"
		self.definitions = [u'in an angry or excited way: ', u'closely and with determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

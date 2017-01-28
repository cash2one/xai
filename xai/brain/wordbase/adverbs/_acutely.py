

#calss header
class _ACUTELY():
	def __init__(self,): 
		self.name = "ACUTELY"
		self.definitions = [u'completely or extremely: ', u'in a very clever or detailed way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

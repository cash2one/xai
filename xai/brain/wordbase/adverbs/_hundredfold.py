

#calss header
class _HUNDREDFOLD():
	def __init__(self,): 
		self.name = "HUNDREDFOLD"
		self.definitions = [u'by a hundred times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

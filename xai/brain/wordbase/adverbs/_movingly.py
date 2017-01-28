

#calss header
class _MOVINGLY():
	def __init__(self,): 
		self.name = "MOVINGLY"
		self.definitions = [u'in a way that causes strong feelings of sadness or sympathy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

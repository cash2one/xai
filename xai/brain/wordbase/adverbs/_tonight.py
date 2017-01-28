

#calss header
class _TONIGHT():
	def __init__(self,): 
		self.name = "TONIGHT"
		self.definitions = [u'(during) the night of the present day: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

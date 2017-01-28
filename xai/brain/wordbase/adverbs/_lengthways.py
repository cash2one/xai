

#calss header
class _LENGTHWAYS():
	def __init__(self,): 
		self.name = "LENGTHWAYS"
		self.definitions = [u'in the direction of the longest side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

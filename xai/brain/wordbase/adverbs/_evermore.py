

#calss header
class _EVERMORE():
	def __init__(self,): 
		self.name = "EVERMORE"
		self.definitions = [u'always in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

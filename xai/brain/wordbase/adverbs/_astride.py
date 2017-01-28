

#calss header
class _ASTRIDE():
	def __init__(self,): 
		self.name = "ASTRIDE"
		self.definitions = [u'with legs wide apart: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

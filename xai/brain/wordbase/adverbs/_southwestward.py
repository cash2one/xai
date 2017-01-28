

#calss header
class _SOUTHWESTWARD():
	def __init__(self,): 
		self.name = "SOUTHWESTWARD"
		self.definitions = [u'towards the southwest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

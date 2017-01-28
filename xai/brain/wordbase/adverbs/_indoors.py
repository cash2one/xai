

#calss header
class _INDOORS():
	def __init__(self,): 
		self.name = "INDOORS"
		self.definitions = [u'into or inside a building: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

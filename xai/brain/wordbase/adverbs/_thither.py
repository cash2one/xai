

#calss header
class _THITHER():
	def __init__(self,): 
		self.name = "THITHER"
		self.definitions = [u'to that place, in that direction']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

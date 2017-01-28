

#calss header
class _TRENCHANT():
	def __init__(self,): 
		self.name = "TRENCHANT"
		self.definitions = [u'severe, expressing strong criticism or forceful opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _MISGUIDED():
	def __init__(self,): 
		self.name = "MISGUIDED"
		self.definitions = [u'unreasonable or unsuitable because of being based on bad judgment or on wrong information or beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

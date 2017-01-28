

#calss header
class _FLAWLESS():
	def __init__(self,): 
		self.name = "FLAWLESS"
		self.definitions = [u'perfect or without mistakes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

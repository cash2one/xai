

#calss header
class _CATTY():
	def __init__(self,): 
		self.name = "CATTY"
		self.definitions = [u'Catty words, especially speech, are unkind because they are intended to hurt someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

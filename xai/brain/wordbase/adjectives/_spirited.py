

#calss header
class _SPIRITED():
	def __init__(self,): 
		self.name = "SPIRITED"
		self.definitions = [u'enthusiastic and determined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

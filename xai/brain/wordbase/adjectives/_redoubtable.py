

#calss header
class _REDOUBTABLE():
	def __init__(self,): 
		self.name = "REDOUBTABLE"
		self.definitions = [u'very strong, especially in character; producing respect and a little fear in others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

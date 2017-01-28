

#calss header
class _BLATANT():
	def __init__(self,): 
		self.name = "BLATANT"
		self.definitions = [u'very obvious and intentional, when this is a bad thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _GUILELESS():
	def __init__(self,): 
		self.name = "GUILELESS"
		self.definitions = [u'honest, not able to deceive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

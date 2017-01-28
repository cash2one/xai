

#calss header
class _STRUCTURED():
	def __init__(self,): 
		self.name = "STRUCTURED"
		self.definitions = [u'organized so that the parts relate well to each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

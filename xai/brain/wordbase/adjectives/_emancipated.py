

#calss header
class _EMANCIPATED():
	def __init__(self,): 
		self.name = "EMANCIPATED"
		self.definitions = [u'not limited socially or politically: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CONDUCTIVE():
	def __init__(self,): 
		self.name = "CONDUCTIVE"
		self.definitions = [u'A conductive substance allows heat or electricity to go through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

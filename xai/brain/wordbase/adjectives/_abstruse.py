

#calss header
class _ABSTRUSE():
	def __init__(self,): 
		self.name = "ABSTRUSE"
		self.definitions = [u'difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

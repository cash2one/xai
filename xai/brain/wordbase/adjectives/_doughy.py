

#calss header
class _DOUGHY():
	def __init__(self,): 
		self.name = "DOUGHY"
		self.definitions = [u'soft, thick, and sticky, like dough']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SUAVE():
	def __init__(self,): 
		self.name = "SUAVE"
		self.definitions = [u'A suave man is very polite, pleasant, and usually attractive, often in a way that is slightly false: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

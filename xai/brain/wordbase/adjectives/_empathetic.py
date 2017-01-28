

#calss header
class _EMPATHETIC():
	def __init__(self,): 
		self.name = "EMPATHETIC"
		self.definitions = [u'having the ability to imagine how someone else feels: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

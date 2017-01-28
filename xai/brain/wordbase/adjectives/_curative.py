

#calss header
class _CURATIVE():
	def __init__(self,): 
		self.name = "CURATIVE"
		self.definitions = [u'able to cure or cause to get better: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

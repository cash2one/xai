

#calss header
class _SLIMMING():
	def __init__(self,): 
		self.name = "SLIMMING"
		self.definitions = [u'Slimming food is food that you can eat without getting fat: ', u'making you look thinner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

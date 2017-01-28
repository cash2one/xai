

#calss header
class _REGRESSIVE():
	def __init__(self,): 
		self.name = "REGRESSIVE"
		self.definitions = [u'(of tax) lower on large amounts of money, so that the rich are less affected']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

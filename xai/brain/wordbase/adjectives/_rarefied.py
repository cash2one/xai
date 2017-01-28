

#calss header
class _RAREFIED():
	def __init__(self,): 
		self.name = "RAREFIED"
		self.definitions = [u'(of air) with little oxygen', u'without any of the problems of ordinary life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SPORTIVE():
	def __init__(self,): 
		self.name = "SPORTIVE"
		self.definitions = [u'having fun and behaving in a way that is not serious: ', u'enjoying sport or relating to sport: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

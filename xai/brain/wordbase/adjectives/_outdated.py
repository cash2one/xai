

#calss header
class _OUTDATED():
	def __init__(self,): 
		self.name = "OUTDATED"
		self.definitions = [u'old-fashioned and therefore not as good or as fashionable as something modern: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

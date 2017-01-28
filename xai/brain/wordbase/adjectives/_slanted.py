

#calss header
class _SLANTED():
	def __init__(self,): 
		self.name = "SLANTED"
		self.definitions = [u'sloping in one direction', u'showing information about one person, one side of an argument, etc. in such a positive or negative way that it is unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

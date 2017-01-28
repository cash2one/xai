

#calss header
class _COLONIAL():
	def __init__(self,): 
		self.name = "COLONIAL"
		self.definitions = [u'relating to a colony or colonialism: ', u'Colonial furniture or buildings are in the style of a period when a country was a colony: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

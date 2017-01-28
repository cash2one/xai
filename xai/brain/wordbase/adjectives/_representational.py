

#calss header
class _REPRESENTATIONAL():
	def __init__(self,): 
		self.name = "REPRESENTATIONAL"
		self.definitions = [u'showing things as they are normally seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _MERCANTILE():
	def __init__(self,): 
		self.name = "MERCANTILE"
		self.definitions = [u'related to trade or business']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

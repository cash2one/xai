

#calss header
class _ENCHANTED():
	def __init__(self,): 
		self.name = "ENCHANTED"
		self.definitions = [u'affected by magic or seeming to be affected by magic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _DISCERNING():
	def __init__(self,): 
		self.name = "DISCERNING"
		self.definitions = [u'showing good judgment, especially about style and quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

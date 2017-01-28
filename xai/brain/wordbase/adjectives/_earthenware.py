

#calss header
class _EARTHENWARE():
	def __init__(self,): 
		self.name = "EARTHENWARE"
		self.definitions = [u'made of quite rough clay, often shaped with the hands: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SEMIPRECIOUS():
	def __init__(self,): 
		self.name = "SEMIPRECIOUS"
		self.definitions = [u'A semiprecious stone is one that is used for making jewellery but is not extremely valuable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

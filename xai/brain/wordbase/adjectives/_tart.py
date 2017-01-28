

#calss header
class _TART():
	def __init__(self,): 
		self.name = "TART"
		self.definitions = [u'(especially of fruit) tasting sour or acidic: ', u'(especially of a way of speaking) quick or sharp and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

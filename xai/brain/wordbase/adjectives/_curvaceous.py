

#calss header
class _CURVACEOUS():
	def __init__(self,): 
		self.name = "CURVACEOUS"
		self.definitions = [u'A curvaceous woman has a body with attractive curves.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

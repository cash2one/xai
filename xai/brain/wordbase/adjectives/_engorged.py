

#calss header
class _ENGORGED():
	def __init__(self,): 
		self.name = "ENGORGED"
		self.definitions = [u'If a part of the body is engorged, it has become swollen or filled with a liquid, especially blood.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

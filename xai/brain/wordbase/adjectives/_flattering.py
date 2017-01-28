

#calss header
class _FLATTERING():
	def __init__(self,): 
		self.name = "FLATTERING"
		self.definitions = [u'making someone look or seem better or more attractive than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

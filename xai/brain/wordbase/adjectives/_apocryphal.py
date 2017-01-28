

#calss header
class _APOCRYPHAL():
	def __init__(self,): 
		self.name = "APOCRYPHAL"
		self.definitions = [u'An apocryphal story is probably not true although it is often told and believed by some people to have happened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

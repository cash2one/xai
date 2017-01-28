

#calss header
class _FACETIOUS():
	def __init__(self,): 
		self.name = "FACETIOUS"
		self.definitions = [u'not serious about a serious subject, in an attempt to be funny or to appear clever : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

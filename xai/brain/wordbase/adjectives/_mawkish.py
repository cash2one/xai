

#calss header
class _MAWKISH():
	def __init__(self,): 
		self.name = "MAWKISH"
		self.definitions = [u'showing emotion or love in an awkward or silly way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

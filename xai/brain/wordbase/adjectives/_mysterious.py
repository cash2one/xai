

#calss header
class _MYSTERIOUS():
	def __init__(self,): 
		self.name = "MYSTERIOUS"
		self.definitions = [u'strange, not known, or not understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

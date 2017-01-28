

#calss header
class _UNIMPEACHABLE():
	def __init__(self,): 
		self.name = "UNIMPEACHABLE"
		self.definitions = [u'of such a high standard of honesty and moral goodness that it cannot be doubted or criticized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SHREDDED():
	def __init__(self,): 
		self.name = "SHREDDED"
		self.definitions = [u'having strong, well-developed muscles that can be seen through the skin, and little body fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

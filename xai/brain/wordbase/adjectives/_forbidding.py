

#calss header
class _FORBIDDING():
	def __init__(self,): 
		self.name = "FORBIDDING"
		self.definitions = [u'unfriendly and likely to be unpleasant or harmful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

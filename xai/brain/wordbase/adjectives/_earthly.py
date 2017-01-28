

#calss header
class _EARTHLY():
	def __init__(self,): 
		self.name = "EARTHLY"
		self.definitions = [u'happening in or relating to this world and this physical life, not in heaven or relating to a spiritual life: ', u'used in questions or negatives to mean possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

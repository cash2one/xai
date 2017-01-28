

#calss header
class _SILURIAN():
	def __init__(self,): 
		self.name = "SILURIAN"
		self.definitions = [u'from or referring to the period of time between about 445 and 420 million years ago, in which fish with jaws (= mouth bones) and some plants and small animals on land first appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

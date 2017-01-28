

#calss header
class _CAMBRIAN():
	def __init__(self,): 
		self.name = "CAMBRIAN"
		self.definitions = [u'from or referring to the period of time between about 543 and 490 million years ago, in which many different types of invertebrates (= animals with no back bone) first appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

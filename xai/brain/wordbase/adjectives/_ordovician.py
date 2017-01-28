

#calss header
class _ORDOVICIAN():
	def __init__(self,): 
		self.name = "ORDOVICIAN"
		self.definitions = [u'from or referring to the period of time between about 485 and 445 million years ago, in which there were many different types of animals in the sea, including vertebrates (= animals with back bones), but no life on land: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

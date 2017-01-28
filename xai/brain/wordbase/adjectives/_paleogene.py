

#calss header
class _PALEOGENE():
	def __init__(self,): 
		self.name = "PALEOGENE"
		self.definitions = [u'from or referring to the period of time between about 66 and 23 million years ago, in which many insects, mammals, and birds appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

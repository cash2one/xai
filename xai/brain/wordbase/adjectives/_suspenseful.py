

#calss header
class _SUSPENSEFUL():
	def __init__(self,): 
		self.name = "SUSPENSEFUL"
		self.definitions = [u'causing a feeling of excitement or nervousness because you are waiting for something to happen or are uncertain about what is going to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

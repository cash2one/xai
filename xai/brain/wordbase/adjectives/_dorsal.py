

#calss header
class _DORSAL():
	def __init__(self,): 
		self.name = "DORSAL"
		self.definitions = [u'of, on, or near the back of an animal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

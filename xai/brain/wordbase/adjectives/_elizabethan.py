

#calss header
class _ELIZABETHAN():
	def __init__(self,): 
		self.name = "ELIZABETHAN"
		self.definitions = [u'from the period when Queen Elizabeth I was the ruler of England (1558-1603)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

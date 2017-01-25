

#calss header
class _PERCEPTIVE():
	def __init__(self,): 
		self.name = "PERCEPTIVE"
		self.jsondata = {}

		self.specie = 'adjectives'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

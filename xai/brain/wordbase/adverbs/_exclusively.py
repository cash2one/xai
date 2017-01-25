

#calss header
class _EXCLUSIVELY():
	def __init__(self,): 
		self.name = "EXCLUSIVELY"
		self.jsondata = {}

		self.specie = 'adverbs'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _THEM():
	def __init__(self,): 
		self.name = "THEM"
		self.jsondata = {}

		self.specie = 'adverbs'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

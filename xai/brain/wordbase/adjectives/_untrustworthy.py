

#calss header
class _UNTRUSTWORTHY():
	def __init__(self,): 
		self.name = "UNTRUSTWORTHY"
		self.jsondata = {}

		self.specie = 'adjectives'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

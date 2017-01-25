

#calss header
class _TUMULTUOUS():
	def __init__(self,): 
		self.name = "TUMULTUOUS"
		self.jsondata = {}

		self.specie = 'adjectives'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

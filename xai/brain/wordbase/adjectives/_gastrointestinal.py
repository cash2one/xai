

#calss header
class _GASTROINTESTINAL():
	def __init__(self,): 
		self.name = "GASTROINTESTINAL"
		self.jsondata = {}

		self.specie = 'adjectives'
		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

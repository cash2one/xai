

#calss header
class _VIVIPAROUS():
	def __init__(self,): 
		self.name = "VIVIPAROUS"
		self.definitions = [u"giving birth to young that have already developed inside the mother's body, rather than producing eggs"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

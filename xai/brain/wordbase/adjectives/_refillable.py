

#calss header
class _REFILLABLE():
	def __init__(self,): 
		self.name = "REFILLABLE"
		self.definitions = [u'A container that is refillable can be filled again when the liquid inside has been used: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

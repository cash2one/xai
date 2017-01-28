

#calss header
class _DRAWN():
	def __init__(self,): 
		self.name = "DRAWN"
		self.definitions = [u'(usually of the face) very tired and showing suffering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SPRIGHTLY():
	def __init__(self,): 
		self.name = "SPRIGHTLY"
		self.definitions = [u'(especially of old people) energetic and in good health: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _INTRINSIC():
	def __init__(self,): 
		self.name = "INTRINSIC"
		self.definitions = [u'being an extremely important and basic characteristic of a person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

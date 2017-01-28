

#calss header
class _FELINE():
	def __init__(self,): 
		self.name = "FELINE"
		self.definitions = [u'belonging or relating to the cat family: ', u'appearing or behaving like a cat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

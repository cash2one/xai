

#calss header
class _PIEBALD():
	def __init__(self,): 
		self.name = "PIEBALD"
		self.definitions = [u'(of an animal, especially a horse) having a pattern of two different colours of hair, especially black and white: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

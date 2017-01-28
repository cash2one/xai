

#calss header
class _PUREBRED():
	def __init__(self,): 
		self.name = "PUREBRED"
		self.definitions = [u'(of an animal or type of animal) with parents that are both of the same breed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _THOROUGHBRED():
	def __init__(self,): 
		self.name = "THOROUGHBRED"
		self.definitions = [u'(a horse) with parents that are of the same breed and have good qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

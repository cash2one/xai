

#calss header
class _BEATIFIC():
	def __init__(self,): 
		self.name = "BEATIFIC"
		self.definitions = [u'appearing happy and calm, especially in a holy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

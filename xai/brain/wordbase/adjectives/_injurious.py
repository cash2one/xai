

#calss header
class _INJURIOUS():
	def __init__(self,): 
		self.name = "INJURIOUS"
		self.definitions = [u'harmful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

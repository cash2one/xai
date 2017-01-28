

#calss header
class _PACKAGED():
	def __init__(self,): 
		self.name = "PACKAGED"
		self.definitions = [u'sold already prepared in a container, usually one made of paper or cardboard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

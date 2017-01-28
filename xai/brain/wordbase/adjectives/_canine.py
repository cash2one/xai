

#calss header
class _CANINE():
	def __init__(self,): 
		self.name = "CANINE"
		self.definitions = [u'of or relating to dogs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

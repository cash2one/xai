

#calss header
class _LADEN():
	def __init__(self,): 
		self.name = "LADEN"
		self.definitions = [u'carrying or holding a lot of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

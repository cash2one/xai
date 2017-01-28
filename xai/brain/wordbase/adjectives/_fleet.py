

#calss header
class _FLEET():
	def __init__(self,): 
		self.name = "FLEET"
		self.definitions = [u'able to run quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

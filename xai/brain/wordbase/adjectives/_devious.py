

#calss header
class _DEVIOUS():
	def __init__(self,): 
		self.name = "DEVIOUS"
		self.definitions = [u'Devious people or plans and methods are dishonest, often in a complicated way, but often also clever and successful: ', u'not direct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

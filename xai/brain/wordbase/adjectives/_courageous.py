

#calss header
class _COURAGEOUS():
	def __init__(self,): 
		self.name = "COURAGEOUS"
		self.definitions = [u'having or showing courage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

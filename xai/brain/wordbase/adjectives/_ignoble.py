

#calss header
class _IGNOBLE():
	def __init__(self,): 
		self.name = "IGNOBLE"
		self.definitions = [u'morally bad and making you feel ashamed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

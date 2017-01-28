

#calss header
class _EVOLVED():
	def __init__(self,): 
		self.name = "EVOLVED"
		self.definitions = [u'having developed through a gradual process: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _TRIED():
	def __init__(self,): 
		self.name = "TRIED"
		self.definitions = [u'used many times before and proved to be successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

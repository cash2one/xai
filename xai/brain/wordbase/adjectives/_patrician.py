

#calss header
class _PATRICIAN():
	def __init__(self,): 
		self.name = "PATRICIAN"
		self.definitions = [u'of or like a person of high social rank']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

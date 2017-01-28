

#calss header
class _BLONDE():
	def __init__(self,): 
		self.name = "BLONDE"
		self.definitions = [u'with pale yellow or gold hair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

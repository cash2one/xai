

#calss header
class _BANAL():
	def __init__(self,): 
		self.name = "BANAL"
		self.definitions = [u'boring, ordinary, and not original: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

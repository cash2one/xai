

#calss header
class _GRAVELLED():
	def __init__(self,): 
		self.name = "GRAVELLED"
		self.definitions = [u'covered with gravel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

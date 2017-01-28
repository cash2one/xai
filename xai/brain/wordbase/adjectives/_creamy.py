

#calss header
class _CREAMY():
	def __init__(self,): 
		self.name = "CREAMY"
		self.definitions = [u'like cream or containing cream: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _HEARTBREAKING():
	def __init__(self,): 
		self.name = "HEARTBREAKING"
		self.definitions = [u'causing extreme sadness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

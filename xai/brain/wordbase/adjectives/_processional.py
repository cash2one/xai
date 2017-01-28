

#calss header
class _PROCESSIONAL():
	def __init__(self,): 
		self.name = "PROCESSIONAL"
		self.definitions = [u'used in a procession: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

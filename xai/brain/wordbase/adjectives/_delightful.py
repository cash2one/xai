

#calss header
class _DELIGHTFUL():
	def __init__(self,): 
		self.name = "DELIGHTFUL"
		self.definitions = [u'very pleasant, attractive, or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

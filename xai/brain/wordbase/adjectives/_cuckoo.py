

#calss header
class _CUCKOO():
	def __init__(self,): 
		self.name = "CUCKOO"
		self.definitions = [u'silly or crazy']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

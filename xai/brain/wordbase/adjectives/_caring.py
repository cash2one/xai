

#calss header
class _CARING():
	def __init__(self,): 
		self.name = "CARING"
		self.definitions = [u'A caring person is kind and gives emotional support to others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _PENULTIMATE():
	def __init__(self,): 
		self.name = "PENULTIMATE"
		self.definitions = [u'second from the last: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

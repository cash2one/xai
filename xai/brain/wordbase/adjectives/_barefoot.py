

#calss header
class _BAREFOOT():
	def __init__(self,): 
		self.name = "BAREFOOT"
		self.definitions = [u'not wearing any shoes or socks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

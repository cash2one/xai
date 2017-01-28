

#calss header
class _UNIMPRESSED():
	def __init__(self,): 
		self.name = "UNIMPRESSED"
		self.definitions = [u'not impressed (= made to feel admiration or respect): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

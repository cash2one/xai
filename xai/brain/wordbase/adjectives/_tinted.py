

#calss header
class _TINTED():
	def __init__(self,): 
		self.name = "TINTED"
		self.definitions = [u'(of glass) with colour added: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

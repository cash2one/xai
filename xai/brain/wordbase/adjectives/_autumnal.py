

#calss header
class _AUTUMNAL():
	def __init__(self,): 
		self.name = "AUTUMNAL"
		self.definitions = [u'typical of autumn: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _BEARISH():
	def __init__(self,): 
		self.name = "BEARISH"
		self.definitions = [u'looking or behaving like a bear', u'expecting a fall in prices: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

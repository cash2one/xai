

#calss header
class _ANGELIC():
	def __init__(self,): 
		self.name = "ANGELIC"
		self.definitions = [u'very beautiful and very good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

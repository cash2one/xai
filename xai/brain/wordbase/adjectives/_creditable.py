

#calss header
class _CREDITABLE():
	def __init__(self,): 
		self.name = "CREDITABLE"
		self.definitions = [u'deserving praise, trust, or respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _ARMOURED():
	def __init__(self,): 
		self.name = "ARMOURED"
		self.definitions = [u'protected by a strong covering, or using military vehicles protected by strong covering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _PENDULOUS():
	def __init__(self,): 
		self.name = "PENDULOUS"
		self.definitions = [u'hanging down loosely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

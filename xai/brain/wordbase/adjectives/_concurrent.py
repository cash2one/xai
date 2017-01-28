

#calss header
class _CONCURRENT():
	def __init__(self,): 
		self.name = "CONCURRENT"
		self.definitions = [u'happening or existing at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

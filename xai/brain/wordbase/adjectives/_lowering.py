

#calss header
class _LOWERING():
	def __init__(self,): 
		self.name = "LOWERING"
		self.definitions = [u'used to describe the sky when it is very dark and it looks as if it is about to rain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

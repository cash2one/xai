

#calss header
class _ROUSING():
	def __init__(self,): 
		self.name = "ROUSING"
		self.definitions = [u'making people feel excited and proud or ready to take action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

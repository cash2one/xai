

#calss header
class _CLAMOROUS():
	def __init__(self,): 
		self.name = "CLAMOROUS"
		self.definitions = [u'making loud demands or complaints', u'making a lot of noise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

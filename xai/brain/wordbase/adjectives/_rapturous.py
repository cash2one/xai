

#calss header
class _RAPTUROUS():
	def __init__(self,): 
		self.name = "RAPTUROUS"
		self.definitions = [u'showing extreme pleasure and happiness or excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

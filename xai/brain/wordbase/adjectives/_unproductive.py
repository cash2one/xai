

#calss header
class _UNPRODUCTIVE():
	def __init__(self,): 
		self.name = "UNPRODUCTIVE"
		self.definitions = [u'not producing very much', u'not having positive results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

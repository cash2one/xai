

#calss header
class _THEREAFTER():
	def __init__(self,): 
		self.name = "THEREAFTER"
		self.definitions = [u'continuing on from a particular point in time, especially after something else has stopped happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

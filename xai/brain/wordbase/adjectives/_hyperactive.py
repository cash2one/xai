

#calss header
class _HYPERACTIVE():
	def __init__(self,): 
		self.name = "HYPERACTIVE"
		self.definitions = [u'Someone who is hyperactive has more energy than is normal, gets excited easily, and cannot stay still or think about work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

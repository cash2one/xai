

#calss header
class _INTERCOLLEGIATE():
	def __init__(self,): 
		self.name = "INTERCOLLEGIATE"
		self.definitions = [u'involving competition between different colleges: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

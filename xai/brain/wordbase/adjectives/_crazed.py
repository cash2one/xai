

#calss header
class _CRAZED():
	def __init__(self,): 
		self.name = "CRAZED"
		self.definitions = [u'behaving in a wild or strange way, especially because of strong emotions or extreme pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

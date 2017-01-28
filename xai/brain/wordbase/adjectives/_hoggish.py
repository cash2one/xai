

#calss header
class _HOGGISH():
	def __init__(self,): 
		self.name = "HOGGISH"
		self.definitions = [u'taking too much for yourself and only thinking about yourself']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

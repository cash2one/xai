

#calss header
class _ARID():
	def __init__(self,): 
		self.name = "ARID"
		self.definitions = [u'very dry and without enough rain for plants: ', u'unsuccessful: ', u'not interesting and showing no imagination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CARELESS():
	def __init__(self,): 
		self.name = "CARELESS"
		self.definitions = [u'not taking or showing enough care and attention: ', u'relaxed, natural, and free from worry']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

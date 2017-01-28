

#calss header
class _CONVIVIAL():
	def __init__(self,): 
		self.name = "CONVIVIAL"
		self.definitions = [u'friendly and making you feel happy and welcome: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

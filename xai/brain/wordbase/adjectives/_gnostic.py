

#calss header
class _GNOSTIC():
	def __init__(self,): 
		self.name = "GNOSTIC"
		self.definitions = [u'relating to knowledge, especially knowledge that most people do not have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

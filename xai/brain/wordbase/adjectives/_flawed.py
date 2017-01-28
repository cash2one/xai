

#calss header
class _FLAWED():
	def __init__(self,): 
		self.name = "FLAWED"
		self.definitions = [u'not perfect, or containing mistakes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

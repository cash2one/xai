

#calss header
class _ASTIR():
	def __init__(self,): 
		self.name = "ASTIR"
		self.definitions = [u'out of bed and moving around, or in an excited state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

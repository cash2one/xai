

#calss header
class _ANOREXIC():
	def __init__(self,): 
		self.name = "ANOREXIC"
		self.definitions = [u'suffering from or relating to anorexia: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

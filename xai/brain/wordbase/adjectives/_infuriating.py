

#calss header
class _INFURIATING():
	def __init__(self,): 
		self.name = "INFURIATING"
		self.definitions = [u'extremely annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _ALCOHOLIC():
	def __init__(self,): 
		self.name = "ALCOHOLIC"
		self.definitions = [u'containing alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

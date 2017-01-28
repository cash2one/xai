

#calss header
class _HYDRAULIC():
	def __init__(self,): 
		self.name = "HYDRAULIC"
		self.definitions = [u'operated by or involving the pressure of water or some other liquid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _STATUTORY():
	def __init__(self,): 
		self.name = "STATUTORY"
		self.definitions = [u'decided or controlled by law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _BLOODCURDLING():
	def __init__(self,): 
		self.name = "BLOODCURDLING"
		self.definitions = [u'causing a feeling of extreme fear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _INIQUITOUS():
	def __init__(self,): 
		self.name = "INIQUITOUS"
		self.definitions = [u'very wrong and unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

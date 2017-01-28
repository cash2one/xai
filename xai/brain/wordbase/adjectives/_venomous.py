

#calss header
class _VENOMOUS():
	def __init__(self,): 
		self.name = "VENOMOUS"
		self.definitions = [u'poisonous: ', u'full of anger or hate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

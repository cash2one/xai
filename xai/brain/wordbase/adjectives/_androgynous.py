

#calss header
class _ANDROGYNOUS():
	def __init__(self,): 
		self.name = "ANDROGYNOUS"
		self.definitions = [u'not clearly male or female: ', u'having both male and female features']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _GRATUITOUS():
	def __init__(self,): 
		self.name = "GRATUITOUS"
		self.definitions = [u'(of something such as bad behaviour) not necessary, or with no cause: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

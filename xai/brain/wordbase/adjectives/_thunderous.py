

#calss header
class _THUNDEROUS():
	def __init__(self,): 
		self.name = "THUNDEROUS"
		self.definitions = [u'extremely loud: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

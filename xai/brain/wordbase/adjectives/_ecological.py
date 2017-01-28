

#calss header
class _ECOLOGICAL():
	def __init__(self,): 
		self.name = "ECOLOGICAL"
		self.definitions = [u'relating to ecology or the environment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

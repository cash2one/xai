

#calss header
class _CAREERS():
	def __init__(self,): 
		self.name = "CAREERS"
		self.definitions = [u'relating to advice about jobs and training: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

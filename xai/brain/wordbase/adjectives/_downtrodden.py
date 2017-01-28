

#calss header
class _DOWNTRODDEN():
	def __init__(self,): 
		self.name = "DOWNTRODDEN"
		self.definitions = [u'treated badly and unfairly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

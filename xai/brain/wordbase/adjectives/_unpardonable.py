

#calss header
class _UNPARDONABLE():
	def __init__(self,): 
		self.name = "UNPARDONABLE"
		self.definitions = [u'(of behaviour) too bad to forgive or be accepted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CORRECTIONAL():
	def __init__(self,): 
		self.name = "CORRECTIONAL"
		self.definitions = [u'relating to the punishment and treatment of people who have committed crimes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

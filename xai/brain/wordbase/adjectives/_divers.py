

#calss header
class _DIVERS():
	def __init__(self,): 
		self.name = "DIVERS"
		self.definitions = [u'various or several']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

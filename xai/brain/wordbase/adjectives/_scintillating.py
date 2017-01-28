

#calss header
class _SCINTILLATING():
	def __init__(self,): 
		self.name = "SCINTILLATING"
		self.definitions = [u'funny, exciting, and clever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _ROOTLESS():
	def __init__(self,): 
		self.name = "ROOTLESS"
		self.definitions = [u'A rootless person does not have a home to return to.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

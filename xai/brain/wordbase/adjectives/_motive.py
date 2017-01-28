

#calss header
class _MOTIVE():
	def __init__(self,): 
		self.name = "MOTIVE"
		self.definitions = [u'(of power or force) causing movement or action']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

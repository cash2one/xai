

#calss header
class _SUSPECT():
	def __init__(self,): 
		self.name = "SUSPECT"
		self.definitions = [u'possibly false or dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _REMOVABLE():
	def __init__(self,): 
		self.name = "REMOVABLE"
		self.definitions = [u'able to be removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _DETACHABLE():
	def __init__(self,): 
		self.name = "DETACHABLE"
		self.definitions = [u'able to be detached: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

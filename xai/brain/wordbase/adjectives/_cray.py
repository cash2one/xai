

#calss header
class _CRAY():
	def __init__(self,): 
		self.name = "CRAY"
		self.definitions = [u'a short form of "crazy" used by some young people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _EXEMPT():
	def __init__(self,): 
		self.name = "EXEMPT"
		self.definitions = [u'with special permission not to do or pay something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

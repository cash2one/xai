

#calss header
class _DEVOID():
	def __init__(self,): 
		self.name = "DEVOID"
		self.definitions = [u'to lack or be without something that is necessary or usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

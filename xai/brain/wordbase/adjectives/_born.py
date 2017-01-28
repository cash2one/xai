

#calss header
class _BORN():
	def __init__(self,): 
		self.name = "BORN"
		self.definitions = [u'having a natural ability or liking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

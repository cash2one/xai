

#calss header
class _UNCEREMONIOUS():
	def __init__(self,): 
		self.name = "UNCEREMONIOUS"
		self.definitions = [u'done in a rude, sudden, or informal way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

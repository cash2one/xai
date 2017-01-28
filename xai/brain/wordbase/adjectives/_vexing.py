

#calss header
class _VEXING():
	def __init__(self,): 
		self.name = "VEXING"
		self.definitions = [u'annoying, worrying, or causing problems : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

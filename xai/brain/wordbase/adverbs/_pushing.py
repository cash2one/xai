

#calss header
class _PUSHING():
	def __init__(self,): 
		self.name = "PUSHING"
		self.definitions = [u'to be almost 50, 60, etc. years old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

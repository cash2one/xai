

#calss header
class _CONTINUAL():
	def __init__(self,): 
		self.name = "CONTINUAL"
		self.definitions = [u'happening repeatedly, usually in an annoying or not convenient way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

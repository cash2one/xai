

#calss header
class _GRIPPING():
	def __init__(self,): 
		self.name = "GRIPPING"
		self.definitions = [u'Something that is gripping is so interesting or exciting that it holds your attention completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SURROGATE():
	def __init__(self,): 
		self.name = "SURROGATE"
		self.definitions = [u'replacing someone else or used instead of something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

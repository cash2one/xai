

#calss header
class _INDECOROUS():
	def __init__(self,): 
		self.name = "INDECOROUS"
		self.definitions = [u'behaving badly or rudely']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _EXTERNAL():
	def __init__(self,): 
		self.name = "EXTERNAL"
		self.definitions = [u'of, on, for, or coming from the outside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

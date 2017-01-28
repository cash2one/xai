

#calss header
class _EXTENSIVE():
	def __init__(self,): 
		self.name = "EXTENSIVE"
		self.definitions = [u'covering a large area; having a great range: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

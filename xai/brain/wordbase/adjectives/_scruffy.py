

#calss header
class _SCRUFFY():
	def __init__(self,): 
		self.name = "SCRUFFY"
		self.definitions = [u'untidy and looking a little dirty : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

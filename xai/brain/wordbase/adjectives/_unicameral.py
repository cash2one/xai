

#calss header
class _UNICAMERAL():
	def __init__(self,): 
		self.name = "UNICAMERAL"
		self.definitions = [u'(of a parliament) having only one group of members: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

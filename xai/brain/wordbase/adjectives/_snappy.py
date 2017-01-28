

#calss header
class _SNAPPY():
	def __init__(self,): 
		self.name = "SNAPPY"
		self.definitions = [u"(especially of a man's clothes or of his appearance) modern and stylish: ", u"immediately effective in getting people's attention or communicating an idea: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

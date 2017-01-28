

#calss header
class _NASCENT():
	def __init__(self,): 
		self.name = "NASCENT"
		self.definitions = [u'only recently formed or started, but likely to grow larger quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

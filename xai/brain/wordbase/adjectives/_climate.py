

#calss header
class _CLIMATE():
	def __init__(self,): 
		self.name = "CLIMATE"
		self.definitions = [u'relating to climate change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

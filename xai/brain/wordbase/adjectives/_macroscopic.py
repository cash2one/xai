

#calss header
class _MACROSCOPIC():
	def __init__(self,): 
		self.name = "MACROSCOPIC"
		self.definitions = [u'large enough to be seen without using any devices that make things look larger']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

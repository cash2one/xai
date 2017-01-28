

#calss header
class _ANTARCTIC():
	def __init__(self,): 
		self.name = "ANTARCTIC"
		self.definitions = [u'belonging or relating to Antarctica or the Antarctic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

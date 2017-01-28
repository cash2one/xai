

#calss header
class _SONIC():
	def __init__(self,): 
		self.name = "SONIC"
		self.definitions = [u'of sound or the speed at which sound travels in air']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

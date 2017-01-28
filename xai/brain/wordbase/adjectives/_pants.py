

#calss header
class _PANTS():
	def __init__(self,): 
		self.name = "PANTS"
		self.definitions = [u'not useful or of bad quality: ', u'belonging or relating to pants: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

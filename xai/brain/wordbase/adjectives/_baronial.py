

#calss header
class _BARONIAL():
	def __init__(self,): 
		self.name = "BARONIAL"
		self.definitions = [u'very large, grand, and impressive: ', u'belonging or relating to a baron: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

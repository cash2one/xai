

#calss header
class _ARMENIAN():
	def __init__(self,): 
		self.name = "ARMENIAN"
		self.definitions = [u'belonging or relating to Armenia, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

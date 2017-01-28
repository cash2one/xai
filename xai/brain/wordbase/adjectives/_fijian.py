

#calss header
class _FIJIAN():
	def __init__(self,): 
		self.name = "FIJIAN"
		self.definitions = [u'belonging to or relating to Fiji, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

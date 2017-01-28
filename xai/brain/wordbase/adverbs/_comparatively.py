

#calss header
class _COMPARATIVELY():
	def __init__(self,): 
		self.name = "COMPARATIVELY"
		self.definitions = [u'as compared to something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

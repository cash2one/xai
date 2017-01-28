

#calss header
class _PREVIOUS():
	def __init__(self,): 
		self.name = "PREVIOUS"
		self.definitions = [u'happening or existing before something or someone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

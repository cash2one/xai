

#calss header
class _UNREAL():
	def __init__(self,): 
		self.name = "UNREAL"
		self.definitions = [u'as if imagined; strange and dream-like: ', u'extremely or surprisingly good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

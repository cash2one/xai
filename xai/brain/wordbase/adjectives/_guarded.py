

#calss header
class _GUARDED():
	def __init__(self,): 
		self.name = "GUARDED"
		self.definitions = [u'careful not to give too much information or show how you really feel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

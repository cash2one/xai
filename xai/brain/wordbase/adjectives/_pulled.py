

#calss header
class _PULLED():
	def __init__(self,): 
		self.name = "PULLED"
		self.definitions = [u'used to describe meat that is cooked slowly until it is very soft, so that it can be easily pulled apart into strips when it is served: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

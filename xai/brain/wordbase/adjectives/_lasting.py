

#calss header
class _LASTING():
	def __init__(self,): 
		self.name = "LASTING"
		self.definitions = [u'continuing to exist for a long time or for ever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

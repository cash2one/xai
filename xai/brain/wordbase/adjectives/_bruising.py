

#calss header
class _BRUISING():
	def __init__(self,): 
		self.name = "BRUISING"
		self.definitions = [u'A bruising experience is one in which someone defeats you or is very rude to you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

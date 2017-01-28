

#calss header
class _INSUFFERABLE():
	def __init__(self,): 
		self.name = "INSUFFERABLE"
		self.definitions = [u'very annoying, unpleasant, or uncomfortable, and therefore extremely difficult to bear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

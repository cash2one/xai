

#calss header
class _EXISTING():
	def __init__(self,): 
		self.name = "EXISTING"
		self.definitions = [u'used to refer to something that exists now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

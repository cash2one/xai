

#calss header
class _UNHINGED():
	def __init__(self,): 
		self.name = "UNHINGED"
		self.definitions = [u'mentally ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CONTEMPORANEOUS():
	def __init__(self,): 
		self.name = "CONTEMPORANEOUS"
		self.definitions = [u'happening or existing at the same period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

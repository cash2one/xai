

#calss header
class _SOCIALIST():
	def __init__(self,): 
		self.name = "SOCIALIST"
		self.definitions = [u'supporting or relating to socialism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

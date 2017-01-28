

#calss header
class _ASYNCHRONOUS():
	def __init__(self,): 
		self.name = "ASYNCHRONOUS"
		self.definitions = [u'not happening or done at the same time or speed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _EVENTFUL():
	def __init__(self,): 
		self.name = "EVENTFUL"
		self.definitions = [u'full of interesting or important events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

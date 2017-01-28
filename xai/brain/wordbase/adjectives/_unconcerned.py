

#calss header
class _UNCONCERNED():
	def __init__(self,): 
		self.name = "UNCONCERNED"
		self.definitions = [u'not worried or not interested, especially when you should be worried or interested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

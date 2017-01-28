

#calss header
class _EXPLORATORY():
	def __init__(self,): 
		self.name = "EXPLORATORY"
		self.definitions = [u'done in order to discover more about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

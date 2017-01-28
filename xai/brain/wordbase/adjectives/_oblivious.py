

#calss header
class _OBLIVIOUS():
	def __init__(self,): 
		self.name = "OBLIVIOUS"
		self.definitions = [u'not conscious of something, especially what is happening around you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

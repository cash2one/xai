

#calss header
class _VEXATIOUS():
	def __init__(self,): 
		self.name = "VEXATIOUS"
		self.definitions = [u'difficult to deal with and causing a lot of anger, worry, or argument: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _PUGNACIOUS():
	def __init__(self,): 
		self.name = "PUGNACIOUS"
		self.definitions = [u'wanting to start an argument or fight, or expressing an argument or opinion very forcefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

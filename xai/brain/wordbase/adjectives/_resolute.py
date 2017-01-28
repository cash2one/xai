

#calss header
class _RESOLUTE():
	def __init__(self,): 
		self.name = "RESOLUTE"
		self.definitions = [u'determined in character, action, or ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

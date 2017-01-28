

#calss header
class _WHIRLWIND():
	def __init__(self,): 
		self.name = "WHIRLWIND"
		self.definitions = [u'A whirlwind event happens very fast, and often unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

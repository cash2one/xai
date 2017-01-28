

#calss header
class _CATCHING():
	def __init__(self,): 
		self.name = "CATCHING"
		self.definitions = [u'If an illness is catching, it can easily be passed from one person to another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

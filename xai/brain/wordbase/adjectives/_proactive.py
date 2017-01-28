

#calss header
class _PROACTIVE():
	def __init__(self,): 
		self.name = "PROACTIVE"
		self.definitions = [u'taking action by causing change and not only reacting to change when it happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

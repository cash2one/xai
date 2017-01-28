

#calss header
class _CONFLICTING():
	def __init__(self,): 
		self.name = "CONFLICTING"
		self.definitions = [u'Conflicting beliefs, needs, facts, etc. are different and opposing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

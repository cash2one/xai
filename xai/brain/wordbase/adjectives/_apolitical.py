

#calss header
class _APOLITICAL():
	def __init__(self,): 
		self.name = "APOLITICAL"
		self.definitions = [u'not interested in or connected with politics, or not connected to any political party: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

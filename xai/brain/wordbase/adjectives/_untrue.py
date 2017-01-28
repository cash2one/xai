

#calss header
class _UNTRUE():
	def __init__(self,): 
		self.name = "UNTRUE"
		self.definitions = [u'not true; false']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

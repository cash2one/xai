

#calss header
class _SELECTIVE():
	def __init__(self,): 
		self.name = "SELECTIVE"
		self.definitions = [u'intentionally choosing some things and not others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

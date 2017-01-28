

#calss header
class _INCONCLUSIVE():
	def __init__(self,): 
		self.name = "INCONCLUSIVE"
		self.definitions = [u'not giving or having a result or decision: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

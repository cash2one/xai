

#calss header
class _QUIESCENT():
	def __init__(self,): 
		self.name = "QUIESCENT"
		self.definitions = [u'temporarily quiet and not active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

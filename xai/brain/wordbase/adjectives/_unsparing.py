

#calss header
class _UNSPARING():
	def __init__(self,): 
		self.name = "UNSPARING"
		self.definitions = [u'showing no kindness and no wish to hide the unpleasant truth: ', u'extremely generous with money, time, help, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

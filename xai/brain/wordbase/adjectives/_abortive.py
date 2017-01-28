

#calss header
class _ABORTIVE():
	def __init__(self,): 
		self.name = "ABORTIVE"
		self.definitions = [u'An abortive attempt or plan has to be stopped because it has failed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _DEMANDING():
	def __init__(self,): 
		self.name = "DEMANDING"
		self.definitions = [u'needing a lot of time, attention, or energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

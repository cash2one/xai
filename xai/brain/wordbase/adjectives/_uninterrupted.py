

#calss header
class _UNINTERRUPTED():
	def __init__(self,): 
		self.name = "UNINTERRUPTED"
		self.definitions = [u'without any pauses or interruptions : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

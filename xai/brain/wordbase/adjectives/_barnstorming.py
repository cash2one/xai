

#calss header
class _BARNSTORMING():
	def __init__(self,): 
		self.name = "BARNSTORMING"
		self.definitions = [u'exciting and energetic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

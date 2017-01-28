

#calss header
class _QUARTERLY():
	def __init__(self,): 
		self.name = "QUARTERLY"
		self.definitions = [u'done or produced four times a year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

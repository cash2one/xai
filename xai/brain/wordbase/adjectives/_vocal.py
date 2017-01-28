

#calss header
class _VOCAL():
	def __init__(self,): 
		self.name = "VOCAL"
		self.definitions = [u'relating to or produced by the voice, either in singing or speaking: ', u'often expressing opinions and complaints in speech: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

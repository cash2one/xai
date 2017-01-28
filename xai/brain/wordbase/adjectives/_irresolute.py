

#calss header
class _IRRESOLUTE():
	def __init__(self,): 
		self.name = "IRRESOLUTE"
		self.definitions = [u'not able or willing to take decisions or actions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

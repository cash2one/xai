

#calss header
class _MONASTIC():
	def __init__(self,): 
		self.name = "MONASTIC"
		self.definitions = [u'connected with monks or monasteries', u'A monastic way of living is simple with few possessions and no people near you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _GRIEVOUS():
	def __init__(self,): 
		self.name = "GRIEVOUS"
		self.definitions = [u'having very serious effects or causing great pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

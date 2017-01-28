

#calss header
class _PARTISAN():
	def __init__(self,): 
		self.name = "PARTISAN"
		self.definitions = [u'strongly supporting a person, principle, or political party, often without considering or judging the matter very carefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

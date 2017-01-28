

#calss header
class _CARDIOVASCULAR():
	def __init__(self,): 
		self.name = "CARDIOVASCULAR"
		self.definitions = [u'relating to the heart and blood vessels (= tubes that carry blood around the body): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

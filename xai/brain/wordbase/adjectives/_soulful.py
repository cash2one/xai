

#calss header
class _SOULFUL():
	def __init__(self,): 
		self.name = "SOULFUL"
		self.definitions = [u'expressing deep feelings, often sadness: ', u'having a deep understanding of and being proud of black culture']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _ASSOCIATE():
	def __init__(self,): 
		self.name = "ASSOCIATE"
		self.definitions = [u'used in the title of a person whose rank is slightly lower or less complete than the full official position described: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

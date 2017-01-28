

#calss header
class _INTERPRETIVE():
	def __init__(self,): 
		self.name = "INTERPRETIVE"
		self.definitions = [u'related to explaining or understanding the meaning of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _UNSURPASSED():
	def __init__(self,): 
		self.name = "UNSURPASSED"
		self.definitions = [u'better than anyone or anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

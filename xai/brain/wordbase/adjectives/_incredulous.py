

#calss header
class _INCREDULOUS():
	def __init__(self,): 
		self.name = "INCREDULOUS"
		self.definitions = [u'not wanting or not able to believe something, and usually showing this: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SAPPY():
	def __init__(self,): 
		self.name = "SAPPY"
		self.definitions = [u'used to describe something that is extremely emotional in an embarrassing way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

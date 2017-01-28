

#calss header
class _PROFITABLE():
	def __init__(self,): 
		self.name = "PROFITABLE"
		self.definitions = [u'resulting in or likely to result in a profit or an advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

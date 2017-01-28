

#calss header
class _UNLISTED():
	def __init__(self,): 
		self.name = "UNLISTED"
		self.definitions = [u'not included in a list of stock exchange company prices: ', u'not included in the public list of phone numbers belonging to the customers of a telephone company: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

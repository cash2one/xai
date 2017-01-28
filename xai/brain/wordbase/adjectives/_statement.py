

#calss header
class _STATEMENT():
	def __init__(self,): 
		self.name = "STATEMENT"
		self.definitions = [u'used to refer to a piece of clothing, jewellery, etc. that is designed to be very noticeable and stylish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

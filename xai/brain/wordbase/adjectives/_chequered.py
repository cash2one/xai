

#calss header
class _CHEQUERED():
	def __init__(self,): 
		self.name = "CHEQUERED"
		self.definitions = [u'having had both successful and unsuccessful periods in your past: ', u'having a pattern of squares in two or more colours: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

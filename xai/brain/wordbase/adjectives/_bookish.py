

#calss header
class _BOOKISH():
	def __init__(self,): 
		self.name = "BOOKISH"
		self.definitions = [u'A bookish person enjoys reading books, especially serious books.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

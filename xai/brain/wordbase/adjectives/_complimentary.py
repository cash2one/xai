

#calss header
class _COMPLIMENTARY():
	def __init__(self,): 
		self.name = "COMPLIMENTARY"
		self.definitions = [u'praising or expressing admiration for someone: ', u'If tickets, books, etc. are complimentary, they are given free, especially by a business.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

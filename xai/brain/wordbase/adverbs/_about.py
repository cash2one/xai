

#calss header
class _ABOUT():
	def __init__(self,): 
		self.name = "ABOUT"
		self.definitions = [u'a little more or less than the stated number or amount: ', u'almost: ', u'in many different directions: ', u'positioned around a place, often without a clear purpose or order: ', u'in or near a place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _FUSSY():
	def __init__(self,): 
		self.name = "FUSSY"
		self.definitions = [u'not easily satisfied, or having very high standards about particular things: ', u'having too much decoration and too many small details, in a way that is not stylish: ', u'A fussy baby is unhappy or difficult to please: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _EVEN():
	def __init__(self,): 
		self.name = "EVEN"
		self.definitions = [u'flat and smooth, or on the same level: ', u'continuous or regular: ', u'equal or equally balanced: ', u'equally likely to happen as to not happen: ', u'used to refer to a situation in which you risk money on something where the risk is equally balanced, and will pay back twice the amount of money that is paid if it is successful: ', u'forming a whole number that can be divided exactly by two: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

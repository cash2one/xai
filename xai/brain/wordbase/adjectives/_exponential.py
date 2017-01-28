

#calss header
class _EXPONENTIAL():
	def __init__(self,): 
		self.name = "EXPONENTIAL"
		self.definitions = [u'An exponential rate of increase becomes quicker and quicker as the thing that increases becomes larger: ', u'containing an exponent (= a number or sign that shows how many times another number is to be multiplied by itself): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

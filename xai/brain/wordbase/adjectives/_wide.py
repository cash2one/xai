

#calss header
class _WIDE():
	def __init__(self,): 
		self.name = "WIDE"
		self.definitions = [u'having a larger distance from one side to the other than is usual or expected, especially in comparison with the length of something; not narrow: ', u'used when describing how long the distance between the two sides of something is or when asking for this information: ', u'used to describe something that includes a large amount or many different types of thing, or that covers a large range or area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

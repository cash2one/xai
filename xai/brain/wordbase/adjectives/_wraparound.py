

#calss header
class _WRAPAROUND():
	def __init__(self,): 
		self.name = "WRAPAROUND"
		self.definitions = [u'(a piece of clothing that is) made so that it can be tied around the body: ', u'(used to describe) something that curves around in one continuous piece']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _WHOLESALE():
	def __init__(self,): 
		self.name = "WHOLESALE"
		self.definitions = [u'of or for the selling of goods in large amounts at low prices to shops and businesses, rather than the selling of goods in shops to customers: ', u'(especially of something bad or too extreme) complete or affecting a lot of things, people, places, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

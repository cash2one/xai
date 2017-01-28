

#calss header
class _SPORTY():
	def __init__(self,): 
		self.name = "SPORTY"
		self.definitions = [u'A sporty person enjoys sport and is good at it: ', u'Sporty clothes are bright and informal, and look like the type of clothes that you could wear for sports.', u'A sporty car is a fast, low car, often for two people only.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

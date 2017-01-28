

#calss header
class _ALLEGED():
	def __init__(self,): 
		self.name = "ALLEGED"
		self.definitions = [u'said or thought by some people to be the stated bad or illegal thing, although you have no proof: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

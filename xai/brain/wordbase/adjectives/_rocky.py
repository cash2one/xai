

#calss header
class _ROCKY():
	def __init__(self,): 
		self.name = "ROCKY"
		self.definitions = [u'made of rock and therefore usually rough and difficult to travel along: ', u'unable to balance very well: ', u'uncertain and difficult and not likely to last long: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

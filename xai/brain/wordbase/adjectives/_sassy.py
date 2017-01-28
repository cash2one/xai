

#calss header
class _SASSY():
	def __init__(self,): 
		self.name = "SASSY"
		self.definitions = [u'rude and showing no respect: ', u'confident or showing confidence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

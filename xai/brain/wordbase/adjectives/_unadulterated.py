

#calss header
class _UNADULTERATED():
	def __init__(self,): 
		self.name = "UNADULTERATED"
		self.definitions = [u'not spoiled or made weaker by the addition of other substances; pure: ', u'complete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

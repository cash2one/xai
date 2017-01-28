

#calss header
class _FLATLY():
	def __init__(self,): 
		self.name = "FLATLY"
		self.definitions = [u'in a way that shows no emotion or interest: ', u'If you flatly deny, refuse, or disagree with something or someone, you do it completely or in a very clear and firm way.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

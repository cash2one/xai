

#calss header
class _LEGITIMATE():
	def __init__(self,): 
		self.name = "LEGITIMATE"
		self.definitions = [u'allowed by law: ', u'reasonable and acceptable: ', u'A legitimate child is one whose parents are legally married at the time of his or her birth.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

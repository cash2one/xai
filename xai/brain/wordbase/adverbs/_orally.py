

#calss header
class _ORALLY():
	def __init__(self,): 
		self.name = "ORALLY"
		self.definitions = [u'expressed in speech, not writing: ', u'entering the body through the mouth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

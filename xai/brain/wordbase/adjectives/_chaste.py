

#calss header
class _CHASTE():
	def __init__(self,): 
		self.name = "CHASTE"
		self.definitions = [u'not having had sex, or only having a sexual relationship with the person you are married to: ', u'used to describe decoration or style that is very simple and smooth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

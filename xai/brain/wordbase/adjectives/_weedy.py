

#calss header
class _WEEDY():
	def __init__(self,): 
		self.name = "WEEDY"
		self.definitions = [u'containing a lot of weeds: ', u'used to describe a person who is thin and physically weak: ', u'weak and not exciting or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

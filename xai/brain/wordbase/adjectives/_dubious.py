

#calss header
class _DUBIOUS():
	def __init__(self,): 
		self.name = "DUBIOUS"
		self.definitions = [u'thought not to be completely true or not able to be trusted: ', u'feeling doubt or not feeling certain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

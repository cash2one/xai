

#calss header
class _REPUTABLE():
	def __init__(self,): 
		self.name = "REPUTABLE"
		self.definitions = [u'having a good reputation and able to be trusted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _BRIEF():
	def __init__(self,): 
		self.name = "BRIEF"
		self.definitions = [u'lasting only a short time or containing few words: ', u'used to express how quickly time goes past: ', u'(of clothes) very short: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

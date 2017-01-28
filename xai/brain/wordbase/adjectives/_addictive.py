

#calss header
class _ADDICTIVE():
	def __init__(self,): 
		self.name = "ADDICTIVE"
		self.definitions = [u'An addictive drug is one that you cannot stop taking once you have started: ', u'An addictive activity or food is one that you cannot stop doing or eating once you have started: ', u'a set of characteristics that mean that you very quickly become addicted to drugs, food, alcohol, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

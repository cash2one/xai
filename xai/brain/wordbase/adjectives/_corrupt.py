

#calss header
class _CORRUPT():
	def __init__(self,): 
		self.name = "CORRUPT"
		self.definitions = [u'dishonestly using your position or power to get an advantage, especially for money: ', u'morally bad: ', u'When information on a computer becomes corrupt, it cannot be used because it has changed and become wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

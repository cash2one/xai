

#calss header
class _SECURELY():
	def __init__(self,): 
		self.name = "SECURELY"
		self.definitions = [u'in a way that avoids someone or something being harmed by any risk, danger, or threat: ', u'positioned or fastened firmly and correctly and therefore not likely to move, fall, or break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

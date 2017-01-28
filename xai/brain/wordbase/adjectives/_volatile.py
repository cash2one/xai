

#calss header
class _VOLATILE():
	def __init__(self,): 
		self.name = "VOLATILE"
		self.definitions = [u'likely to change suddenly and unexpectedly or suddenly become violent or angry: ', u'A volatile liquid or solid substance will change easily into a gas.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

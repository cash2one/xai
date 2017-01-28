

#calss header
class _UNROMANTIC():
	def __init__(self,): 
		self.name = "UNROMANTIC"
		self.definitions = [u'not doing things to show your love for your partner: ', u'not very exciting or special: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

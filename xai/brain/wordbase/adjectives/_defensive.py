

#calss header
class _DEFENSIVE():
	def __init__(self,): 
		self.name = "DEFENSIVE"
		self.definitions = [u'used to protect someone or something against attack: ', u'too quick to protect yourself from being criticized: ', u'in a sports event, trying to prevent the opposing player or players from scoring points, goals, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

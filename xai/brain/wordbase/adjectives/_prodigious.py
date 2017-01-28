

#calss header
class _PRODIGIOUS():
	def __init__(self,): 
		self.name = "PRODIGIOUS"
		self.definitions = [u'extremely great in ability, amount, or strength: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

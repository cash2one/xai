

#calss header
class _SOLVENT():
	def __init__(self,): 
		self.name = "SOLVENT"
		self.definitions = [u'(especially of companies) having enough money to pay all the money that is owed to other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

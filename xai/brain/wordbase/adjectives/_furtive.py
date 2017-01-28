

#calss header
class _FURTIVE():
	def __init__(self,): 
		self.name = "FURTIVE"
		self.definitions = [u'(of people) behaving secretly and often dishonestly, or (of actions) done secretly and often dishonestly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

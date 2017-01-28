

#calss header
class _OVERDRAWN():
	def __init__(self,): 
		self.name = "OVERDRAWN"
		self.definitions = [u'having taken more money out of your bank account than the account contained, or (of a bank account) having had more money taken from it than was originally in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _VITUPERATIVE():
	def __init__(self,): 
		self.name = "VITUPERATIVE"
		self.definitions = [u'A vituperative spoken or written attack is full of angry criticism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _MERCENARY():
	def __init__(self,): 
		self.name = "MERCENARY"
		self.definitions = [u'interested only in the amount of money that you can get from a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

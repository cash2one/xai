

#calss header
class _EFFERVESCENT():
	def __init__(self,): 
		self.name = "EFFERVESCENT"
		self.definitions = [u'An effervescent liquid produces bubbles of gas: ', u'active, positive, and full of energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

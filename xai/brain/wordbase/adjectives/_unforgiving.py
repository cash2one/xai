

#calss header
class _UNFORGIVING():
	def __init__(self,): 
		self.name = "UNFORGIVING"
		self.definitions = [u'not willing to forgive people for things they do wrong: ', u'unpleasant or difficult to deal with: ', u'An unforgiving fabric or item of clothing can make you look fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

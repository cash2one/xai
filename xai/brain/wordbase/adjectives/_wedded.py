

#calss header
class _WEDDED():
	def __init__(self,): 
		self.name = "WEDDED"
		self.definitions = [u'believing firmly in an idea or theory and unwilling to change that belief: ', u'married: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

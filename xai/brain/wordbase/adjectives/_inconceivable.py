

#calss header
class _INCONCEIVABLE():
	def __init__(self,): 
		self.name = "INCONCEIVABLE"
		self.definitions = [u'impossible to imagine or think of: ', u'extremely unlikely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

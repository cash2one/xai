

#calss header
class _STEREOTYPICAL():
	def __init__(self,): 
		self.name = "STEREOTYPICAL"
		self.definitions = [u'having the qualities that you expect a particular type of person to have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

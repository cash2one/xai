

#calss header
class _PRIMARY():
	def __init__(self,): 
		self.name = "PRIMARY"
		self.definitions = [u'more important than anything else; main: ', u'of or for the teaching of young children, especially those between five and eleven years old: ', u'happening first: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

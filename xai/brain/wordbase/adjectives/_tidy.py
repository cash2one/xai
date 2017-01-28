

#calss header
class _TIDY():
	def __init__(self,): 
		self.name = "TIDY"
		self.definitions = [u'having everything ordered and arranged in the right place, or liking to keep things like this: ', u'(of amounts of money) large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

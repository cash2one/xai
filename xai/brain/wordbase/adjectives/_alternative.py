

#calss header
class _ALTERNATIVE():
	def __init__(self,): 
		self.name = "ALTERNATIVE"
		self.definitions = [u'An alternative plan or method is one that you can use if you do not want to use another one: ', u'Alternative things are considered to be unusual and often have a small but enthusiastic group of people who support them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

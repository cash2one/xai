

#calss header
class _POSSIBLE():
	def __init__(self,): 
		self.name = "POSSIBLE"
		self.definitions = [u'able to be done or achieved, or able to exist: ', u'as much, quickly, soon, etc. as something can happen or be done: ', u'that might or might not happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

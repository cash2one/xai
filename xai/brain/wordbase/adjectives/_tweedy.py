

#calss header
class _TWEEDY():
	def __init__(self,): 
		self.name = "TWEEDY"
		self.definitions = [u'of or like tweed: ', u'used to describe the life of rich people with homes in the countryside and an interest in horses, dogs, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

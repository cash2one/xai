

#calss header
class _PRACTISED():
	def __init__(self,): 
		self.name = "PRACTISED"
		self.definitions = [u'very good at doing something because you have a lot of experience of doing it: ', u'A practised skill has been obtained from a lot of practice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

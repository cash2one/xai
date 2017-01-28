

#calss header
class _CHARITABLE():
	def __init__(self,): 
		self.name = "CHARITABLE"
		self.definitions = [u'giving money, food, or help free to those who are in need because they are ill, poor, or have no home: ', u'kind, and not judging other people in a severe way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

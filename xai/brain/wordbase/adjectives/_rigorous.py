

#calss header
class _RIGOROUS():
	def __init__(self,): 
		self.name = "RIGOROUS"
		self.definitions = [u'careful to look at or consider every part of something to make certain it is correct or safe: ', u'controlling behaviour in a severe way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

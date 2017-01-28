

#calss header
class _SWEEPING():
	def __init__(self,): 
		self.name = "SWEEPING"
		self.definitions = [u'affecting many things or people; large: ', u'something that you say or write that is too general and that has not been carefully thought about: ', u'A sweeping win or victory is an easy or complete win: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

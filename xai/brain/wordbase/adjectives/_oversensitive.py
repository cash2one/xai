

#calss header
class _OVERSENSITIVE():
	def __init__(self,): 
		self.name = "OVERSENSITIVE"
		self.definitions = [u'too easily upset: ', u'damaged, changed, or harmed by something that would not affect most people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

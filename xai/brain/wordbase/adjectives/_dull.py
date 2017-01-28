

#calss header
class _DULL():
	def __init__(self,): 
		self.name = "DULL"
		self.definitions = [u'not interesting or exciting in any way: ', u'not clear, bright, or shiny: ', u'A dull sound or pain is not sharp or clear: ', u'not intelligent']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

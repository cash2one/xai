

#calss header
class _BRIGHT():
	def __init__(self,): 
		self.name = "BRIGHT"
		self.definitions = [u'full of light, shining: ', u'strong in colour: ', u'intelligent and quick to learn: ', u'full of hope for success or happiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

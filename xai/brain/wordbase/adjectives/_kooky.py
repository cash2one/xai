

#calss header
class _KOOKY():
	def __init__(self,): 
		self.name = "KOOKY"
		self.definitions = [u'(especially of a person) strange in his or her appearance or behaviour, especially in a way that is interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

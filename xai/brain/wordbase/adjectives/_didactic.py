

#calss header
class _DIDACTIC():
	def __init__(self,): 
		self.name = "DIDACTIC"
		self.definitions = [u'intended to teach, especially in a way that is too determined or eager, and often fixed and unwilling to change: ', u'intended to teach people a moral lesson: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

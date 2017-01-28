

#calss header
class _FIGURATIVE():
	def __init__(self,): 
		self.name = "FIGURATIVE"
		self.definitions = [u'(of words and phrases) used not with their basic meaning but with a more imaginative meaning, in order to create a special effect: ', u'(of a painting, drawing, etc.) representing something as it really looks, rather than in an abstract way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

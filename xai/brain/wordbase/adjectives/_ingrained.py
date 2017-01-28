

#calss header
class _INGRAINED():
	def __init__(self,): 
		self.name = "INGRAINED"
		self.definitions = [u'(of beliefs) so firmly held that they are not likely to change: ', u'Ingrained dirt has got under the surface of something and is difficult to remove: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

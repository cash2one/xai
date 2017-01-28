

#calss header
class _FASHIONABLE():
	def __init__(self,): 
		self.name = "FASHIONABLE"
		self.definitions = [u'popular at a particular time: ', u'wearing clothes, doing things, and going to places that are in fashion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

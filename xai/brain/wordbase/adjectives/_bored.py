

#calss header
class _BORED():
	def __init__(self,): 
		self.name = "BORED"
		self.definitions = [u'feeling unhappy because something is not interesting or because you have nothing to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _PRETTY():
	def __init__(self,): 
		self.name = "PRETTY"
		self.definitions = [u'pleasant to look at, or (especially of girls or women or things relating to them) attractive or pleasant in a delicate way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

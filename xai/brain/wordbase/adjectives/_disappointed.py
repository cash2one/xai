

#calss header
class _DISAPPOINTED():
	def __init__(self,): 
		self.name = "DISAPPOINTED"
		self.definitions = [u'unhappy because someone or something was not as good as you hoped or expected, or because something did not happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

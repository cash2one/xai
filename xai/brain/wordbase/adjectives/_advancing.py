

#calss header
class _ADVANCING():
	def __init__(self,): 
		self.name = "ADVANCING"
		self.definitions = [u"If you talk about someone's advancing age, you mean that they are getting older: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

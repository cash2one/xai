

#calss header
class _ANSWERABLE():
	def __init__(self,): 
		self.name = "ANSWERABLE"
		self.definitions = [u'to be responsible for something that happens: ', u'If you are answerable to someone, you have to explain your actions to them because they have the main control and responsibility: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

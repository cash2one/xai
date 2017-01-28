

#calss header
class _PECULIAR():
	def __init__(self,): 
		self.name = "PECULIAR"
		self.definitions = [u'unusual and strange, sometimes in an unpleasant way: ', u'belonging to, relating to, or found in only particular people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

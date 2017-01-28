

#calss header
class _UNITARY():
	def __init__(self,): 
		self.name = "UNITARY"
		self.definitions = [u'of a system of local government in the UK in which official power is given to one organization that deals with all matters in a local area instead of to several organizations that each deal with only a few matters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

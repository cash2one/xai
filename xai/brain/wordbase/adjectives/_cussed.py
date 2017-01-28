

#calss header
class _CUSSED():
	def __init__(self,): 
		self.name = "CUSSED"
		self.definitions = [u'used to describe people who are unwilling to be helpful, or things that are annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

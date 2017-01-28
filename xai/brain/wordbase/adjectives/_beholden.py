

#calss header
class _BEHOLDEN():
	def __init__(self,): 
		self.name = "BEHOLDEN"
		self.definitions = [u'feeling you have a duty to someone because they have done something for you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

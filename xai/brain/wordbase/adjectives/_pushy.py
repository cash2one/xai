

#calss header
class _PUSHY():
	def __init__(self,): 
		self.name = "PUSHY"
		self.definitions = [u'behaving in an unpleasant way by trying too much to get something or to make someone do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

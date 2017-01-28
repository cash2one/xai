

#calss header
class _DETESTABLE():
	def __init__(self,): 
		self.name = "DETESTABLE"
		self.definitions = [u'used to refer to people or things that you hate very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

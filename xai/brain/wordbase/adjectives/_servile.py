

#calss header
class _SERVILE():
	def __init__(self,): 
		self.name = "SERVILE"
		self.definitions = [u'too eager to serve and please someone else in a way that shows you do not have much respect for yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

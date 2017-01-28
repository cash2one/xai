

#calss header
class _WAYWARD():
	def __init__(self,): 
		self.name = "WAYWARD"
		self.definitions = [u'doing only what you want and often changing your behaviour in a way that is difficult to control']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

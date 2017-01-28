

#calss header
class _SEMINAL():
	def __init__(self,): 
		self.name = "SEMINAL"
		self.definitions = [u'containing important new ideas and having a great influence on later work: ', u'connected with semen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

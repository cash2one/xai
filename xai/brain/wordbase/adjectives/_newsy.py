

#calss header
class _NEWSY():
	def __init__(self,): 
		self.name = "NEWSY"
		self.definitions = [u'containing a lot of news that is personal or not very serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

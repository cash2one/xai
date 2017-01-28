

#calss header
class _OFFHAND():
	def __init__(self,): 
		self.name = "OFFHAND"
		self.definitions = [u'without looking for information and without thinking carefully; immediately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _CRUNCHY():
	def __init__(self,): 
		self.name = "CRUNCHY"
		self.definitions = [u'Crunchy food is firm and makes a loud noise when it is eaten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

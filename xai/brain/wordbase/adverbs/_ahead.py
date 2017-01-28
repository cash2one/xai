

#calss header
class _AHEAD():
	def __init__(self,): 
		self.name = "AHEAD"
		self.definitions = [u'in front: ', u'having more points, votes, etc. than someone else in a competition, election, etc.: ', u'making more progress than someone else: ', u'in or into the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

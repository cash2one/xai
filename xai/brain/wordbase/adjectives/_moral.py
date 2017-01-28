

#calss header
class _MORAL():
	def __init__(self,): 
		self.name = "MORAL"
		self.definitions = [u'relating to the standards of good or bad behaviour, fairness, honesty, etc. that each person believes in, rather than to laws: ', u'behaving in ways considered by most people to be correct and honest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

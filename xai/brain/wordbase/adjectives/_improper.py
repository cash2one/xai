

#calss header
class _IMPROPER():
	def __init__(self,): 
		self.name = "IMPROPER"
		self.definitions = [u'dishonest and against a law or a rule: ', u'unsuitable or not correct for a particular use or occasion: ', u'related to sex in a way that is rude or socially unacceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

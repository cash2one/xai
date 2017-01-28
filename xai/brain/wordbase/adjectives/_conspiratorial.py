

#calss header
class _CONSPIRATORIAL():
	def __init__(self,): 
		self.name = "CONSPIRATORIAL"
		self.definitions = [u"relating to a secret plan to do something bad, illegal, or against someone's wishes", u'showing that you share a secret: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

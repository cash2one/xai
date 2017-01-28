

#calss header
class _UNYIELDING():
	def __init__(self,): 
		self.name = "UNYIELDING"
		self.definitions = [u'completely unwilling to change a decision, opinion, demand, etc.: ', u'rigid (= not able to be bent or moved)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

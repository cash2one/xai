

#calss header
class _STUBBORN():
	def __init__(self,): 
		self.name = "STUBBORN"
		self.definitions = [u'A stubborn person is determined to do what he or she wants and refuses to do anything else: ', u'Things that are stubborn are difficult to move, change, or deal with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

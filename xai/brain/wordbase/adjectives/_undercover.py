

#calss header
class _UNDERCOVER():
	def __init__(self,): 
		self.name = "UNDERCOVER"
		self.definitions = [u'working secretly using a false appearance in order to get information for the police or government: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

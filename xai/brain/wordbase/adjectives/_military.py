

#calss header
class _MILITARY():
	def __init__(self,): 
		self.name = "MILITARY"
		self.definitions = [u'relating to or belonging to the armed forces: ', u'typical of the armed forces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

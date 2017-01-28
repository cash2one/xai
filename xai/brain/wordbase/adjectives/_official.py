

#calss header
class _OFFICIAL():
	def __init__(self,): 
		self.name = "OFFICIAL"
		self.definitions = [u'relating to a position of responsibility: ', u'agreed to or arranged by people in positions of authority: ', u'If a piece of information is official, it has been announced publicly with authority: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _UNDECIDED():
	def __init__(self,): 
		self.name = "UNDECIDED"
		self.definitions = [u'If you are undecided, you have not yet made a decision or judgment about something: ', u'not decided or finished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

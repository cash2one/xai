

#calss header
class _SEARCHING():
	def __init__(self,): 
		self.name = "SEARCHING"
		self.definitions = [u'intended to find out the often hidden truth about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

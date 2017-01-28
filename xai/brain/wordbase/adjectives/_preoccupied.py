

#calss header
class _PREOCCUPIED():
	def __init__(self,): 
		self.name = "PREOCCUPIED"
		self.definitions = [u'thinking or worrying about something too much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

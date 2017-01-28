

#calss header
class _HEARTENED():
	def __init__(self,): 
		self.name = "HEARTENED"
		self.definitions = [u'feeling happier and more positive about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

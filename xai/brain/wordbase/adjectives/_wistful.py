

#calss header
class _WISTFUL():
	def __init__(self,): 
		self.name = "WISTFUL"
		self.definitions = [u'sad and thinking about something that is impossible or in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

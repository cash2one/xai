

#calss header
class _PUMPED():
	def __init__(self,): 
		self.name = "PUMPED"
		self.definitions = [u'excited about something that is going to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

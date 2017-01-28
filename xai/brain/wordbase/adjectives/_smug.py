

#calss header
class _SMUG():
	def __init__(self,): 
		self.name = "SMUG"
		self.definitions = [u'too pleased or satisfied about something you have achieved or something you know: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

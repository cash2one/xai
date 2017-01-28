

#calss header
class _UNINFORMED():
	def __init__(self,): 
		self.name = "UNINFORMED"
		self.definitions = [u'not knowing much or having much information about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _LYRICAL():
	def __init__(self,): 
		self.name = "LYRICAL"
		self.definitions = [u'expressing personal thoughts and feelings in a beautiful way: ', u'to talk about something with a lot of interest or excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

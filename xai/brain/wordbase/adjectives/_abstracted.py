

#calss header
class _ABSTRACTED():
	def __init__(self,): 
		self.name = "ABSTRACTED"
		self.definitions = [u'not giving attention to what is happening around you because you are thinking about something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

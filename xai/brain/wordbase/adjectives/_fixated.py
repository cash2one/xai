

#calss header
class _FIXATED():
	def __init__(self,): 
		self.name = "FIXATED"
		self.definitions = [u'unable to stop thinking about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _STOKED():
	def __init__(self,): 
		self.name = "STOKED"
		self.definitions = [u'excited and very happy about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

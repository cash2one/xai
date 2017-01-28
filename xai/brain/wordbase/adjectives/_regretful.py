

#calss header
class _REGRETFUL():
	def __init__(self,): 
		self.name = "REGRETFUL"
		self.definitions = [u'showing that you feel sorry about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

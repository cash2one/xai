

#calss header
class _TREASONABLE():
	def __init__(self,): 
		self.name = "TREASONABLE"
		self.definitions = [u'A treasonable act, crime, etc. is, or is considered to be, treason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

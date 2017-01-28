

#calss header
class _SCURRILOUS():
	def __init__(self,): 
		self.name = "SCURRILOUS"
		self.definitions = [u"expressing unfair or false criticism that is likely to damage someone's reputation: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

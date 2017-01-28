

#calss header
class _POSTOPERATIVE():
	def __init__(self,): 
		self.name = "POSTOPERATIVE"
		self.definitions = [u'relating to the period of time that immediately follows a medical operation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _INCHOATE():
	def __init__(self,): 
		self.name = "INCHOATE"
		self.definitions = [u'only recently or partly formed, or not completely developed or clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

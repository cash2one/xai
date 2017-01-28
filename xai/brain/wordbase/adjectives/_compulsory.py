

#calss header
class _COMPULSORY():
	def __init__(self,): 
		self.name = "COMPULSORY"
		self.definitions = [u'If something is compulsory, you must do it because of a rule or law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

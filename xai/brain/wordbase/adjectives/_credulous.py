

#calss header
class _CREDULOUS():
	def __init__(self,): 
		self.name = "CREDULOUS"
		self.definitions = [u'too willing to believe what you are told and so easily deceived']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

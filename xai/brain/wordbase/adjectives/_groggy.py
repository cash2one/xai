

#calss header
class _GROGGY():
	def __init__(self,): 
		self.name = "GROGGY"
		self.definitions = [u'weak and unable to think clearly or walk correctly, usually because of tiredness or illness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

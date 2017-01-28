

#calss header
class _PERSUASIVE():
	def __init__(self,): 
		self.name = "PERSUASIVE"
		self.definitions = [u'making you want to do or believe a particular thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _DOCILE():
	def __init__(self,): 
		self.name = "DOCILE"
		self.definitions = [u'quiet and easy to influence, persuade, or control: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

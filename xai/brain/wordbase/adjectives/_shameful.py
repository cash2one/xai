

#calss header
class _SHAMEFUL():
	def __init__(self,): 
		self.name = "SHAMEFUL"
		self.definitions = [u'deserving blame, or being a reason for feeling ashamed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

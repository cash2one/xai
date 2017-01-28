

#calss header
class _VENGEFUL():
	def __init__(self,): 
		self.name = "VENGEFUL"
		self.definitions = [u'expressing a strong wish to punish someone who has harmed you or your family or friends: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

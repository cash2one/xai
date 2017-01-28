

#calss header
class _VARSITY():
	def __init__(self,): 
		self.name = "VARSITY"
		self.definitions = [u'used to describe sports teams at schools or colleges that are at the most skilled level of play: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _FLIGHTY():
	def __init__(self,): 
		self.name = "FLIGHTY"
		self.definitions = [u'(especially of a woman) not responsible and likely to change activities, jobs, boyfriends, etc. often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

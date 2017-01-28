

#calss header
class _UNAPPROACHABLE():
	def __init__(self,): 
		self.name = "UNAPPROACHABLE"
		self.definitions = [u'Someone who is unapproachable seems unfriendly or a little frightening, so that other people are less likely to speak to them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

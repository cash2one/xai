

#calss header
class _AFOUL():
	def __init__(self,): 
		self.name = "AFOUL"
		self.definitions = [u'to experience problems, punishment, or harm because you do not obey a rule or disagree with a powerful organization, group, or person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

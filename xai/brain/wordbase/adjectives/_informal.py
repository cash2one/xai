

#calss header
class _INFORMAL():
	def __init__(self,): 
		self.name = "INFORMAL"
		self.definitions = [u'(of situations) not formal or official, or (of clothing, behaviour, speech) suitable when you are with friends and family but not for official occasions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

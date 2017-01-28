

#calss header
class _OBSCENE():
	def __init__(self,): 
		self.name = "OBSCENE"
		self.definitions = [u'offensive, rude, or shocking, usually because of being too obviously related to sex or showing sex: ', u'morally wrong, often describing something that is wrong because it is too large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _STRIDENT():
	def __init__(self,): 
		self.name = "STRIDENT"
		self.definitions = [u'A strident sound is loud, unpleasant, and rough: ', u'expressing or expressed in forceful language that does not try to avoid upsetting other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

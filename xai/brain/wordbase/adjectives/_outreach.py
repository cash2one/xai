

#calss header
class _OUTREACH():
	def __init__(self,): 
		self.name = "OUTREACH"
		self.definitions = [u'bringing medical or other services to people at home or to where they spend time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

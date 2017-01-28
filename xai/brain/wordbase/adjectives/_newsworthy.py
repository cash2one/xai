

#calss header
class _NEWSWORTHY():
	def __init__(self,): 
		self.name = "NEWSWORTHY"
		self.definitions = [u'interesting enough to be described in a news report: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

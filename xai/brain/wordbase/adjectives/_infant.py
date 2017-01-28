

#calss header
class _INFANT():
	def __init__(self,): 
		self.name = "INFANT"
		self.definitions = [u'related to or connected with the first stage of school in the UK, for children aged four to seven years: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

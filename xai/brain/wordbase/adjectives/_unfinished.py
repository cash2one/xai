

#calss header
class _UNFINISHED():
	def __init__(self,): 
		self.name = "UNFINISHED"
		self.definitions = [u'not ended or completed', u'a matter, especially a disagreement, that is not yet decided or agreed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

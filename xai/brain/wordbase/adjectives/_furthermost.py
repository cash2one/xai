

#calss header
class _FURTHERMOST():
	def __init__(self,): 
		self.name = "FURTHERMOST"
		self.definitions = [u'The furthermost place or places are those at the greatest distance away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

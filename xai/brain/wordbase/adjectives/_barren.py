

#calss header
class _BARREN():
	def __init__(self,): 
		self.name = "BARREN"
		self.definitions = [u'unable to produce plants or fruit: ', u'unable to have children or young animals', u'not creating or producing anything new: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

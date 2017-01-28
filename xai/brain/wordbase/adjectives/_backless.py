

#calss header
class _BACKLESS():
	def __init__(self,): 
		self.name = "BACKLESS"
		self.definitions = [u"not covering most of a person's back: ", u'with no back part: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

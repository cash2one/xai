

#calss header
class _APPOSITE():
	def __init__(self,): 
		self.name = "APPOSITE"
		self.definitions = [u'suitable and right for the occasion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

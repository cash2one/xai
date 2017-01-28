

#calss header
class _AUTONOMOUS():
	def __init__(self,): 
		self.name = "AUTONOMOUS"
		self.definitions = [u'independent and having the power to make your own decisions', u'an autonomous organization, country, or region is independent and has the freedom to govern itself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

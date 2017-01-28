

#calss header
class _RHEUMY():
	def __init__(self,): 
		self.name = "RHEUMY"
		self.definitions = [u'rheumy eyes have a lot of water in them and are not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

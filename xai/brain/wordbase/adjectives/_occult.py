

#calss header
class _OCCULT():
	def __init__(self,): 
		self.name = "OCCULT"
		self.definitions = [u'relating to magical powers and activities, such as those of witchcraft and astrology: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

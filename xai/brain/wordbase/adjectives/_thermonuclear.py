

#calss header
class _THERMONUCLEAR():
	def __init__(self,): 
		self.name = "THERMONUCLEAR"
		self.definitions = [u'relating to nuclear reactions that happen only at very high temperatures, or to weapons that make use of such reactions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

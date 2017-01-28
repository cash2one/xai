

#calss header
class _SWANKY():
	def __init__(self,): 
		self.name = "SWANKY"
		self.definitions = [u"very expensive and fashionable, in a way that is intended to attract people's attention and admiration: ", u'behaving too confidently: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _UNHEARD():
	def __init__(self,): 
		self.name = "UNHEARD"
		self.definitions = [u'to not be listened to or considered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

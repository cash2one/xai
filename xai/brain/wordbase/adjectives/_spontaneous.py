

#calss header
class _SPONTANEOUS():
	def __init__(self,): 
		self.name = "SPONTANEOUS"
		self.definitions = [u'happening or done in a natural, often sudden way, without any planning or without being forced: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

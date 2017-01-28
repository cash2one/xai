

#calss header
class _TONAL():
	def __init__(self,): 
		self.name = "TONAL"
		self.definitions = [u'relating to the quality of sound of a musical instrument or singing voice', u'Tonal music is music that is based on major and minor keys.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

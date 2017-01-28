

#calss header
class _GILDED():
	def __init__(self,): 
		self.name = "GILDED"
		self.definitions = [u'covered with a thin layer of gold or a substance that looks like gold: ', u'rich or of a higher social class: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

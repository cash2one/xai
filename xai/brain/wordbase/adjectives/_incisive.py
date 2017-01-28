

#calss header
class _INCISIVE():
	def __init__(self,): 
		self.name = "INCISIVE"
		self.definitions = [u'expressing an idea or opinion in a clear and direct way that shows good understanding of what is important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
